#![allow(non_snake_case)] // fixin some shit error abt snake stuff

fn main() 
{
    // Notez
    // mut means u can change var -         let mut var: i32 = 69;
    // lack of 'mut' gives u error if u reassign var
    // int be of 2 types 'i' and 'u' and then followed by the int type like, 8, 16, 32, 64, 128 etc. u can add size to make it defaut
    // for float the same syntax but replace i/u with f
    // dividing 2 float givs exact answer... but dividing 2 floats givs math.floor()-ed answer
    // bool iz true false
    // char is depicted with '', string is depicted with ""
    // tup (tuple) iz defined az            let tup: (vartype, vartype...)=(var, var...);
    // u can get deconstruct by saying             let (x, y...) = tup    - dis gives corresponding data to x, y.. seperately
    // get val of tup by doin           tup.0           or whatever index of num
    // haz to be same var type in array; size cannot be changed - like c#... array type be written like      let var: [vartype:length] = array
    //  or u can also type (for same value of each element in array)             let var: [element_val, length]
    // access elements with [] - like c# and python
    


    //      ==========================================STUFF TO DO========================================

    //                  TF U DOIN!!! MEAK USER NUMBER THING GO UN_BRRRRRRRRRRR...   UPREESHEYATED
    
    extern crate serde;

    use std::io;        // import std.io
    use firebase_rs::Firebase;
    use serde::{Serialize, Deserialize};

    #[derive(Debug, Serialize, Deserialize)]
    
    enum General
    {
        Number(usize),
        None
    }

    let origroom = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap(); // setup firebase
    let roomData = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap(); // setup firebase
    let room = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap();
    let playerdata = Firebase::new("https://maifurztruztprojekt-default-rtdb.firebaseio.com/roomz.json").unwrap();



    println!("Enter name of room: ");
    let mut roomname= String::new();
    io::stdin()                 // yeet name into str name and give error msg if error 'unaybal 3 reed laiyne'
        .read_line(&mut roomname) // Get room
        .expect("unaybal 2 reed laiyne");
    

    println!("Enter your name: ");
    let mut name= String::new();
    io::stdin()                 // Get name
        .read_line(&mut name)
        .expect("unaybal 2 reed laiyne");

    let room=room.at(&roomname).unwrap().at("players").unwrap();
    let origroom=origroom.at(&roomname).unwrap();
    let roomData=roomData.at(&roomname).unwrap().at("data").unwrap();
    let playerdata=playerdata.at(&roomname).unwrap().at("PlayerData").unwrap();
    let res=roomData.update("{\"PlayerTurn\":\"0\", \"TotalMoney\":\"69420\", \"UsernameOffset\":\"0\"}");
    println!("Room Data Response: {:?}", res);
    let res=playerdata.at(&name).unwrap().update("{\"Money\":\"0\", \"Eco\":\"0\", \"IGNORE\":\"0\", \"LEAVE\":\"0\"}");
    println!("{:?}", res);
    println!("{:?}", room.get().unwrap().body);
    let usernum: usize = if room.get().unwrap().body!="null"
    {
        room.get_generic::<Vec<String>>().unwrap().data.len()
    }
    else
    {
        0
    };
    
    let data = format!("{{\"{}\":\"{}\"}}", usernum, name.trim());
    let res=room.update(&data).unwrap();
    println!("Room Players Response: {:?}", res);

    print!("joined {}", roomname);

    let roomcopy=room.clone();
    GameLoop(roomData, room, playerdata, usernum, name.clone());

    // tmp
    leevRoom(roomcopy, origroom, usernum, name);
}

fn GameLoop(roomData: firebase_rs::Firebase, room:firebase_rs::Firebase, playerdata:firebase_rs::Firebase, usernum:usize, name:String)
{
    use std::io;
    use std::collections::HashMap;

    println!("GameLoop");
    let mut new_turn_stored:isize=-1; // for the player turn msg
    let mut new_turn_eco:isize=-1; // for eco
    loop
    {   
        let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;
        let mut tot_ignorz=0;
        for (_key, val) in hashmapdata.iter()
        {
            if val.get("LEAVE").unwrap().trim()=="1"
            {
                tot_ignorz=tot_ignorz+1;
            }
        }
        if tot_ignorz==room.get_generic::<Vec<String>>().unwrap().data.len()
        {
            return;
        }
        let hashmapdata=roomData.get_generic::<HashMap<String, String>>().unwrap().data;
        let offset = hashmapdata.get("UsernameOffset").unwrap().trim().parse::<usize>().unwrap();
        let mut new_turn=hashmapdata.get("PlayerTurn").unwrap().trim().parse::<usize>().unwrap();


        // eco
        
        if new_turn==0 && new_turn_eco!=new_turn as isize
        {
            let res=playerdata.at(&name.trim()).unwrap().update(&format!("{{\"Money\":\"{}\"}}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()+playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Eco").unwrap().trim().parse::<usize>().unwrap()));
            println!("{:?}", res);
        }
        new_turn_eco=new_turn as isize;

        if new_turn==usernum
        {
            println!("It's your turn to play!\n");
            println!("'+' - increases your money by 50\n'eco' - increases your eco; costs 50 money");


            // command
            let mut valid="U no type :(";
            while valid!="Ogae"
            {
                println!("Whatchu wanna do?");
                let mut add= String::new();
                io::stdin()                 // Get name
                    .read_line(&mut add)
                    .expect("unaybal 2 reed laiyne");

                if add.to_owned().trim()=="+"
                {
                    let res=playerdata.at(&name.trim()).unwrap().update(&format!("{{\"Money\":\"{}\"}}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()+50));
                    println!("{:?}", res);
                    valid="Ogae";
                }
                else if add.to_owned().trim()=="eco"
                {
                    if playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()>=50
                    {
                        let res=playerdata.at(&name.trim()).unwrap().update(&format!("{{\"Eco\":\"{}\"}}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Eco").unwrap().trim().parse::<usize>().unwrap()+100));
                        println!("{:?}", res);
                        valid="Ogae";
                    }
                    else
                    {
                        valid="U broke! lmfao";
                    }
                }
                println!("{}", valid);
            }
            
            


            // winning
            let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;
            if hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()>=100
            {
                println!("You win the game!");
                let res=playerdata.update(&format!("{{\"{}\":{{\"Money\":\"{}\", \"Eco\":\"{}\", \"IGNORE\":\"1\", \"LEAVE\":\"0\"}}}}", name.trim(), hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Eco").unwrap().trim()));
                println!("{:?}", res);
            }


            //data
            let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;         

            tot_ignorz=0;
            for (_key, val) in hashmapdata.iter()
            {
                if val.get("IGNORE").unwrap().trim()=="1"
                {
                    tot_ignorz=tot_ignorz+1;
                }
            }
            if tot_ignorz<room.get_generic::<Vec<String>>().unwrap().data.len()
            {
                println!("{} < {}", tot_ignorz, room.get_generic::<Vec<String>>().unwrap().data.len());

                new_turn=if new_turn+1==room.get_generic::<Vec<String>>().unwrap().data.len()
                {0}
                else
                {new_turn+1};
                let new_turn_player_name=&room.get_generic::<Vec<String>>().unwrap().data[new_turn];
                while playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(new_turn_player_name).unwrap().get("IGNORE").unwrap().trim()=="1"
                {
                    new_turn=if new_turn+1==room.get_generic::<Vec<String>>().unwrap().data.len()
                    {0}
                    else
                    {new_turn+1};
                }
            }

            let res=roomData.update(&format!("{{\"PlayerTurn\":\"{}\", \"TotalMoney\":\"69420\", \"UsernameOffset\":\"{}\"}}", new_turn, offset));
            println!("Room Data Response: {:?}\n", res);

            println!("{}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("IGNORE").unwrap().trim());
            if playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("IGNORE").unwrap().trim()=="1"
            {
                let res=playerdata.update(&format!("{{\"{}\":{{\"Money\":\"{}\", \"Eco\":\"{}\", \"IGNORE\":\"1\", \"LEAVE\":\"1\"}}}}", name.trim(), hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Eco").unwrap().trim()));
                println!("{:?}", res);
            }
        }
        else
        {
            if new_turn as isize!=new_turn_stored
            {
                println!("It's {}'s turn to play!\n", room.get_generic::<Vec<String>>().unwrap().data[new_turn]);
                new_turn_stored=new_turn as isize;
            }
        }
    }
}

fn leevRoom(_room: firebase_rs::Firebase, origroom:firebase_rs::Firebase, usernum: usize, _name:String)
{
    if usernum==0
    {
        let res=origroom.delete("*");
        println!("{:?}", res);
    }

}