class View:
  GREET = '''
Умею складывать "+", вычитать "-", умножать "*" и делить "/" два числа.
А также возводить число в степень "^".
Для использования введи число, затем мат. операцию и снова число.
Числа и мат. операцию отделяй пробелом, например: 2 * 2
  '''


  def render_greet(self):
    print(self.GREET)


  def render_input(self):
    return input('Введите выражение: ')


  def render_result(self, result):
    print(f"Результат: {result:g}")
