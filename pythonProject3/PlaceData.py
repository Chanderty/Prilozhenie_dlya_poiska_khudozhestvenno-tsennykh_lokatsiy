def create_m():
    class object:
        def __init__(self, id, tag, name, placename = "", des=""):
            self.placename = placename
            self.id = id
            self.tag = tag
            self.name = name
            self.des = des
        def __repr__(self):
            return f"|{self.id} {self.tag} {self.name} {self.des}|"

    a = []

    a.append(object(0, ("дятел", "птица", "лес"), "1", "Pic1", "Большой пестрый дятел в поисках пищи\nАвтор: Баранов А.С."))
    a.append(object(1, ("цветы", "поле"), "2", "Pic2", "Полевые колокольчики\nАвтор: Баранов А.С."))
    a.append(object(2, ("гриб", "лес"), "3", "Pic3", "Белый гриб в еловом бору\nАвтор: Баранов А.С."))
    a.append(object(3, ("гриб", "слизень", "лес"), "4", "Pic4", "Трапеза большого слизня\nАвтор: Баранов А.С."))
    a.append(object(4, ("белка", "лес", "зима"), "5", "Pic5", "Пушистая обитательница зимнего леса\nАвтор: Баранов А.С."))
    a.append(object(5, ("синица", "птица", "лес", "зима"), "6", "Pic6", "Синица в зимнем лесу\nАвтор: Баранов А.С."))
    a.append(object(6, ("озеро", "зима", "вечер"), "7", "Pic7", "Белая пустошь замерзшего озера\nАвтор: Баранов А.С."))
    a.append(object(7, ("река", "зима"), "8", "Pic8", "Зимняя сказка\nАвтор: Баранов А.С."))
    a.append(object(8, ("архитектура", "город"), "9", "Pic9", "Королев во всей красе\nАвтор: Баранов А.С."))
    a.append(object(9, ("архитектура", "храм", "зима"), "10", "Pic10", "Сельский храм\nАвтор: Баранов А.С."))
    a.append(object(10, ("лес", "дорога"), "11", "Pic11", "Лесная тропа\nАвтор: Баранов А.С."))
    a.append(object(11, ("архитектура", "город", "вечер"), "12", "Pic12", "Дальний мегаполис\nАвтор: Баранов А.С."))
    return a
