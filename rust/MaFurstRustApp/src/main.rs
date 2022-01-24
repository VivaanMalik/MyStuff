#![allow(non_snake_case)] // fixin some shit error abt snake stuff

extern crate rand;

use rand::distributions::Distribution;
use rand::distributions::Uniform;
use std::{thread, time};
use std::collections::HashMap;


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

    // USE THIS ARE 4 TESTINGG



    // AHHHHH

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
    let res=playerdata.at(&name).unwrap().update("{\"Money\":\"0\", \"Eco\":\"0\", \"IGNORE\":\"0\", \"LEAVE\":\"0\", \"Itemz\":\"Basic_Sword\"}");
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

    println!("GameLoop");
    let mut new_turn_stored:isize=-1; // for the player turn msg

    let itemdata=giveitemdata();
    println!("{:?}", itemdata);
    let mut adventure=false;

    loop
    {   
        let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;

        // println!("ITEMZ: {:?}", itemz);
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

        if new_turn==usernum && !adventure
        {
            let res=playerdata.at(&name.to_owned().trim()).unwrap().update(&format!("{{\"Money\":\"{}\"}}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()+playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Eco").unwrap().trim().parse::<usize>().unwrap()));
            println!("eco: {:?}", res);

            println!("It's your turn to play!\n");
            println!("Type 'info' to see all commands...");


            // command
            let mut valid="U no type :(";
            while valid!="Ogae"
            {
                valid="U no type :(";
                println!("Whatchu wanna do? You haz {} money, {} eco...", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim(), playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Eco").unwrap().trim());
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
                        let res=playerdata.at(&name.trim()).unwrap().update(&format!("{{\"Eco\":\"{}\", \"Money\":\"{}\"}}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Eco").unwrap().trim().parse::<usize>().unwrap()+100, playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()-50));
                        println!("{:?}", res);
                        valid="Ogae";
                    }
                    else
                    {
                        valid="U broke! lmfao";
                    }
                }
                else if add.to_owned().trim()=="hunt"
                {
                    adventure=true;
                    valid="Ogae";
                }
                else if add.to_owned().trim()=="weapons"
                {
                    println!
(
"\nWEAPONS\n
Basic Sword       1    Damage    10   Endurance    50  Cost    The Start to your journey to become the devil...
Blazefury         1K   Damage    15K  Endurance    1K  Cost    FFFIIIRREE!!!
Nirvana           20K  Damage    1M   Endurance    50K Cost    Champion Of Chaos
Unholy Might      350K Damage    1B   Endurance    2M  Cost    Buthcer of the serpent\n"
);
                    valid="Learn, kid ↑";
                }
                else if add.to_owned().trim()=="info"
                {
                    println!
(
"\nINFO\n
+        - Increase your money by 50; Buy powerups/items with money
eco      - Increase your eco by 100; Eco gives you money every time its your turn
info     - Get this list
hunt     - Go on a hunt to collect loot
weapons  - Get list of weapons along with its info\n"
);
                    valid="Learn, kid ↑";
                }
                println!("{}", valid);
            }
            
            


            // winning
            let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;
            if hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim().parse::<usize>().unwrap()>=100
            {
                println!("You win the game!");
                let res=playerdata.update(&format!("{{\"{}\":{{\"Money\":\"{}\", \"Eco\":\"{}\", \"IGNORE\":\"1\", \"LEAVE\":\"0\", \"Itemz\":\"{}\"}}}}", name.trim(), hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Eco").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Itemz").unwrap().trim()));
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
            if tot_ignorz<room.get_generic::<Vec<String>>().unwrap().data.len()-1
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

            if adventure
            {
                let _res=playerdata.at(&name.trim()).unwrap().update("{\"IGNORE\":\"1\"}");
            }

            let res=roomData.update(&format!("{{\"PlayerTurn\":\"{}\", \"TotalMoney\":\"69420\", \"UsernameOffset\":\"{}\"}}", new_turn, offset));
            println!("Room Data Response: {:?}\n", res);

            println!("{}", playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("IGNORE").unwrap().trim());
            if playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data.get(name.trim()).unwrap().get("IGNORE").unwrap().trim()=="1"
            {
                if !adventure
                {
                    let res=playerdata.update(&format!("{{\"{}\":{{\"Money\":\"{}\", \"Eco\":\"{}\", \"IGNORE\":\"1\", \"LEAVE\":\"1\", \"Itemz\":\"{}\"}}}}", name.trim(), hashmapdata.get(name.trim()).unwrap().get("Money").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Eco").unwrap().trim(), hashmapdata.get(name.trim()).unwrap().get("Itemz").unwrap().trim()));
                    println!("{:?}", res);
                }
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



        if adventure
        {
            println!("Searching for monsters to hunt...");
            thread::sleep(time::Duration::from_secs(randrange(3, 6)));
            let soul=GenerateSoul();
            let mut valid="U no type valid :(";

            while valid!="Ogae"
            {
                let mut response=String::new();
                valid="U no type valid :(";
                println!("AHA! You found a{} named {}\nType 'info' to get all commands to hunt\n", AorAn(soul.get("type").unwrap().to_string().to_ascii_lowercase()), soul.get("name").unwrap().to_string());
                io::stdin()
                    .read_line(&mut response)
                    .expect("unaybal 2 reed laiyne");
                if response.to_owned().trim()=="end hunt"
                {
                    adventure=false;
                    valid="Ogae";
                }
                else if response.to_owned().trim()=="items"
                {
                    let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;
                    let items=getplayeritems(hashmapdata, name.clone());
                    println!("\nYOUR ITEMS\n");
                    let mut biggestnum:usize=0;
                    for i in &items
                    {
                        if i.len()>biggestnum
                        {
                            biggestnum=i.len();
                        }
                    }
                    for mut i in items
                    {
                        let itemsinfo=get_item_info_from_item_name(giveitemdata(), i.clone());
                        while i.len()<biggestnum
                        {
                            i=format!("{} ", i);
                        }
                        println!("{}          Damage {}          Endurance {}          Cost {}", i, pretty_print_nums(*itemsinfo.get("Damage").unwrap(), 1), pretty_print_nums(*itemsinfo.get("Endurance").unwrap(), 1), pretty_print_nums(*itemsinfo.get("Cost").unwrap(), 1));
                    }
                    valid="Learn, kid ↑\n";
                }
                else if response.to_owned().trim().starts_with("use")
                {
                    let hashmapdata=playerdata.get_generic::<HashMap<String, HashMap<String, String>>>().unwrap().data;
                    let split=response.trim().split("use ").collect::<Vec<&str>>();
                    if getplayeritems(hashmapdata, name.clone()).contains(&split[split.clone().len()-1].to_string())
                    {
                        // damage
                        valid="Ogae";
                    }
                    else
                    {
                        valid="Breh, u need to have that item ┑(￣Д ￣)┍\n";
                    }
                }
                else if response.to_owned().trim()=="info"
                {
                    println!
(
"\nINFO\n
end hunt   - Go back to main game
items      - Get info on all your items and their name
use [Item] - Use an item to your advantage or the enemies disadvantage
info       - Get this list\n"
);
                    valid="Learn, kid ↑\n";
                }
                println!("{}", valid);
            }

            if !adventure
            {
                let _res=playerdata.at(name.trim()).unwrap().update("{\"IGNORE\":\"0\"}");
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

fn giveitemdata() -> HashMap<String, HashMap<String, usize>>
{
    let info = vec![String::from("Damage"), String::from("Endurance"), String::from("Cost")];
    let infovalz = vec![1, 10, 50];
    let basicsword: HashMap<_, _> = info.into_iter().zip(infovalz.into_iter()).collect();

    let info = vec![String::from("Damage"), String::from("Endurance"), String::from("Cost")];
    let infovalz = vec![1000, 15000, 1000];
    let blazefury: HashMap<_, _> = info.into_iter().zip(infovalz.into_iter()).collect();

    let info = vec![String::from("Damage"), String::from("Endurance"), String::from("Cost")];
    let infovalz = vec![20000, 1000000, 50000];
    let nirvana: HashMap<_, _> = info.into_iter().zip(infovalz.into_iter()).collect();

    let info = vec![String::from("Damage"), String::from("Endurance"), String::from("Cost")];
    let infovalz = vec![350000, 1000000000, 2000000];
    let unholymight: HashMap<_, _> = info.into_iter().zip(infovalz.into_iter()).collect();

    let info= vec![String::from("Basic Sword"), String::from("Blazefury"), String::from("Nirvana"), String::from("Unholy Might")];
    let infovalz = vec![basicsword, blazefury, nirvana, unholymight];
    let itemdata: HashMap<String, HashMap<String, usize>> = info.into_iter().zip(infovalz.into_iter()).collect();

    return itemdata;
}

fn GenerateSoul() -> HashMap<String, String>
{
    let randnum=randrange(0, 9);
    use rnglib::{RNG, Language};
    let rng = RNG::new(&Language::Fantasy).unwrap();
    let name = rng.generate_name_by_count(3);
    let mut soul: HashMap<String, _>=HashMap::new();
    soul.insert("name".to_string(), name);
    let types=["Goblin", "Zombie", "Orc", "Ghoul", "Troll", "Elf", "Ogre", "Giant", "Oni", "Kraken"];
    soul.insert("power".to_string(), format!("{}", randnum*randrange(5, 10)));
    soul.insert("type".to_string(), types[randnum as usize].to_string());
    return soul;
}

fn randrange(a:u64, b:u64) -> u64
{
    return Uniform::new_inclusive(a, b).sample(&mut rand::thread_rng())
}

fn AorAn(string:String) -> String
{
    let vowels: [char; 5] = ['a', 'e', 'i', 'o', 'u'];
    if vowels.contains(&string.trim().to_ascii_lowercase().chars().next().unwrap())
    {
        return format!("n {}", &string.trim()).to_string();
    }
    else
    {
        println!("{}", &string.trim().chars().next().unwrap());
        return format!(" {}", &string.trim()).to_string();
    }
}

fn getplayeritems(hashmapdata:HashMap<String, HashMap<String, String>>, name:String) -> Vec<String>
{
    return hashmapdata.get(name.trim()).unwrap().get("Itemz").unwrap().trim().split_whitespace().map(|word| word.parse::<String>().unwrap().replace("_", " ")).collect::<Vec<_>>();
}

fn get_item_info_from_item_name(hashmap:HashMap<String, HashMap<String, usize>>, itemname:String) -> HashMap<String, usize>
{
    return hashmap.get(&itemname).unwrap().to_owned();
}

fn pretty_print_nums(num:usize, addspaces:usize) -> String
{
    let mut num:String=format!("{}", num);
    let amntof000s=num.matches("000").count();
    let mut zeros=String::new();
    for _ in 0..amntof000s
    {
        zeros=format!("{}000", zeros);
    }
    let suffix=["", "K", "M", "B", "T", "Qua", "Qui", "Si", "Se", "Oct", "N", "Dec"];
    let pos:usize=num.rfind(&zeros).unwrap();
    let endpos:usize = pos+zeros.len();
    let replacestring=suffix[amntof000s];
    num.replace_range(pos..endpos, replacestring);
    if addspaces!=0
    {
        while num.len()!=6
        {
            if addspaces==1
            {
                num=format!("{} ", num);
            }
            else
            {
                num=format!(" {}", num);
            }
        }
    }
    return num;
}