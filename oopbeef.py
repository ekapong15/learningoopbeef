# ปิ้งย่าง

class Beef:

    def __init__(self,name,cooking,dryage):
        self.name = name
        self.cooking = cooking
        self.dryage = int(dryage)

    def cook(self):
        print(f'สั่ง{self.name}แล้ว{self.cooking}ดิคับ')

    def howto(self):
        if self.cooking == 'ย่าง':
            print(f'อย่า{self.cooking}{self.name}นาน มันจะไม่อร่อย')
        else:
            print(f'ให้ชุบไข่ก่อน{self.cooking} จะได้นุ่มๆ')

    def eat(self):
        print('พักให้มันเย็นสักแปบบ แล้วแด๊กเลย')
            

class HiBeef(Beef):
    def __init__(self,name,cooking,dryage,grade):
        super().__init__(name,cooking,dryage)
        self.grade = grade
    
    def howto(self):
        if self.grade == 'a5':
            print(f'{self.cooking}30วิก็พอ เดียว{self.name}มันจะแข็ง')
        else:
            print(f'{self.cooking}สัก1นาที')

    def eat(self):
        print('ของมันแพง อย่าให้เหลือ')
        print(f'หวานกว่าน้ำตาลก็มัน{self.name}นี่แหละ')

if __name__ == '__main__':
    osaka = HiBeef('เนื้อโอซาก้า','ย่าง', 14 , 'a3')
    mutsusaka = HiBeef('เนื้อมัสซึซากะ','ย่าง', 30, 'a4')
    wakyu = HiBeef('เนื้อวากิว','เซียร์', 45, 'a5')

    thaislide = Beef('เนื้อสไลด์ไทย','ต้ม', 7)
    thaisteak = Beef('เนื้อสไลด์ไทย','ย่าง', 14)

    print(thaislide.cook())
    print(thaislide.howto())
    print(thaislide.eat())
    print(wakyu.cook())
    print(osaka.cook())
    print(wakyu.howto())
    print(osaka.howto())
    print(osaka.eat())



