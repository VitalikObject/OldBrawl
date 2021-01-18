class PlayerHome:
    def encodeHome(self, packet):
        #player info#
        packet.writeVint(2018007) #first timestamp
        packet.writeVint(0) #second timestamp
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        
        packet.writeVint(28) #icons csv id
        packet.writeVint(0) #icon
        
        packet.writeVint(9) #array 1
        packet.writeVint(0)
        packet.writeVint(2)
        packet.writeVint(3)
        packet.writeVint(5)
        packet.writeVint(6)
        packet.writeVint(7)
        packet.writeVint(8)
        packet.writeVint(9)
        packet.writeVint(10)
        
        packet.writeVint(0) #array 2
        
        packet.writeVint(0) #array 3
        
        packet.writeByte(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeByte(0)
        packet.writeVint(0)
        packet.writeByte(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeByte(0)
        
        packet.writeVint(16) #datareference ???
        packet.writeVint(0)
        
        packet.writeByte(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeByte(0)
        
        packet.writeVint(0) #array v8
        
        packet.writeVint(0) #array v10
        
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        
        packet.writeVint(0) #array v12
        
        packet.writeVint(0)
        #player info end#
        
        #sub_251FCA#
        
        packet.writeVint(2019053)
        packet.writeVint(100)
        packet.writeVint(10)
        packet.writeVint(30)
        packet.writeVint(3)
        packet.writeVint(80)
        packet.writeVint(10)
        packet.writeVint(50)
        packet.writeVint(1000)
        packet.writeVint(500)
        packet.writeVint(50)
        packet.writeVint(999900)
        
        packet.writeVint(0) #ShopArray
        
        packet.writeVint(8) #array 1
        packet.writeVint(1)
        packet.writeVint(2)
        packet.writeVint(3)
        packet.writeVint(4)
        packet.writeVint(5)
        packet.writeVint(6)
        packet.writeVint(7)
        packet.writeVint(8)
        
        packet.writeVint(4) #массивчик events
        
        for x in range(4):
            packet.writeVint(0)
            packet.writeVint(x)
            packet.writeVint(0)
            packet.writeVint(75992)
            packet.writeVint(10)
            
            packet.writeVint(15)
            packet.writeVint(2)
            
            packet.writeVint(3)
            packet.writeString()
            packet.writeVint(0)
        
        packet.writeVint(0) #event array empty
        
        packet.writeVint(8) # ????
        for x in [20, 35, 75, 140, 290, 480, 800, 1250]:
            packet.writeVint(x)

        packet.writeVint(8) # ????
        for x in [1, 2, 3, 4, 5, 10, 15, 20]:
            packet.writeVint(x)

        packet.writeVint(3)
        for x in [10, 30, 80]: # Tickets Amount
            packet.writeVint(x)

        packet.writeVint(3) 
        for x in [6, 20, 60]: # Tickets Count
            packet.writeVint(x)

        packet.writeVint(4) 
        for x in [20, 50, 140, 280]: # Gold Amount
            packet.writeVint(x)

        packet.writeVint(4)
        for x in [150, 400, 1200, 2600]: # Gold Count
            packet.writeVint(x)
        
        packet.writeVint(0)
        
        packet.writeVint(2) #sub_119716
        packet.writeVint(200)
        packet.writeVint(20)
        
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        
        #sub_251FCA end#
        
        packet.writeInt(0)
        packet.writeInt(0)
        
        packet.writeVint(0) #array

    def encodeAvatar(self, packet):
        packet.writeVint(0)
        packet.writeVint(1)
        packet.writeVint(0)
        packet.writeVint(1)
        packet.writeVint(0)
        packet.writeVint(1)
        
        packet.writeString("RetroBrawl")
        
        packet.writeByte(1)
        
        packet.writeInt(0)
        
        packet.writeVint(0) #commodity
        
        packet.writeVint(0)
        
        #packet.writeVint(23)
        #packet.writeVint(0)
        #packet.writeVint(1)
        
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)
        packet.writeVint(0)