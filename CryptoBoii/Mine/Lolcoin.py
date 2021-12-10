## Imports

import hashlib
import time


class Block:

    """

    How a Block Looks:

    {
    "Index": 2,
    "ProofNum": 21,
    "PrevHash": "6e27587e8a27d6fe376d4fd9b4edc96c8890346579e5cbf558252b24a8257823",
    "transactions": [
        {'sender': '0', 'recipient': 'Quincy Larson', 'quantity': 1}
    ],
    "timestamp": 1521646442.4096143
    }
    
    """

    def __init__(self, Index, ProofNum, PrevHash, Data, TimeStamp=None):
        self.Index=Index
        self.ProofNum=ProofNum
        self.PrevHash=PrevHash
        self.Data=Data
        self.TimeStamp=TimeStamp or time.time()

    @property
    def CalculateHash(self):
        """
        Calulation of Da cryptographic hash 
        """
        BlockOfString="{}{}{}{}{}".format(self.Index, self.ProofNum, self.PrevHash, self.Data, self.TimeStamp)
        return hashlib.sha256(BlockOfString.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.Index, self.ProofNum, self.PrevHash, self.Data, self.TimeStamp)  

class BlockChain:

    def __init__(self):
        self.Chain=[]
        self.CurrentData=[]
        self.Nodes=set()
        self.ConstructGenesisBlock()

    def ConstructGenesisBlock(self):
        """
        Create initial block
        """
        self.ConstructBlock(ProofNum=0, PrevHash=0)

    def ConstructBlock(self, ProofNum, PrevHash):
        """
        constructs the next blocks in chain
        """
        block=Block(Index=len(self.Chain), ProofNum=ProofNum, PrevHash=PrevHash, Data=self.CurrentData)
        self.CurrentData=[]
        self.Chain.append(block)
        return block

    @staticmethod
    def CheckValidity(block, PrevBlock):
        """
        Check if block chain == valid
        """
        if PrevBlock.Index + 1 != block.Index:
            return False

        elif PrevBlock.CalculateHash != block.PrevHash:
            return False

        elif not BlockChain.VerifyProof(block.ProofNum, PrevBlock.ProofNum):
            return False

        elif block.TimeStamp <= PrevBlock.TimeStamp:
            return False
        return True

    def NewData(self, Sender, Recipient, Amount):
        """
        appends new transactional data to da existing data
        """
        self.CurrentData.append({'Sender':Sender, 'Recipient':Recipient, 'Amount':Amount})
        return True

    @staticmethod
    def ProofOfWork(PrevProof):
        ProofNum=0
        while BlockChain.VerifyProof(ProofNum, PrevProof) is False:
            ProofNum+=1
        return ProofNum
    
    @staticmethod
    def VerifyProof(PrevProof, Proof):
        Guess=f'{PrevProof}{Proof}'.encode()
        GuessHash=hashlib.sha256(Guess).hexdigest()
        return GuessHash[:4]=="0000"


    @property
    def LatestBlock(self):
        return self.Chain[-1]

    def BlockMining(self, DetailsMiner):
        self.NewData(Sender='0', Recipient=DetailsMiner, Amount=1)
        LastBlock=self.LatestBlock
        LastProofNum=LastBlock.ProofNum
        ProofNum=self.ProofOfWork(LastProofNum)
        LastHash=LastBlock.CalculateHash
        block=self.ConstructBlock(ProofNum, LastHash)
        return vars(block)
        
    def CreateNode(self, Address):
        self.Nodes.add(Address)
        return True
    
    def ObtainBlockObj(BlockData):
        return Block(BlockData['Index'], BlockData['ProofNum'], BlockData['PrevHash'], BlockData['Data'], TimeStamp=BlockData['TimeStamp'])
    
blockchain=BlockChain()
print("Starting Da Mining of Da LolCoin!!!")
print(blockchain.Chain)
lastblock=blockchain.LatestBlock
lastproofno=lastblock.ProofNum
proofno=blockchain.ProofOfWork(lastproofno)
blockchain.NewData(Sender='0', Recipient="[Insert Name]", Amount=1)
lasthash=lastblock.CalculateHash
block=blockchain.ConstructBlock(proofno, lasthash)
print("successssss")
print(blockchain.Chain)