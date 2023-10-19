class Student:
  def __init__(self, student_id, nome, idade, mae, pai):
      self.student_id = student_id
      self.nome = nome  
      self.idade = idade
      self.mae = mae
      self.pai = pai

class StudentDatabase:
  def __init__(self):
      self.students = []

  def create_student(self, student_id, nome, idade, mae, pai):
      student = Student(student_id, nome, idade, mae, pai)
      self.students.append(student)

  def read_student(self, student_id):
      for student in self.students:
          if student.student_id == student_id:
              return student
      return None

  def update_student(self, student_id, nome, idade, mae, pai):
      for student in self.students:
          if student.student_id == student_id:
              student.nome = nome
              student.idade = idade
              student.mae = mae
              student.pai = pai
              return True
      return False

  def delete_student(self, student_id):
      for student in self.students:
          if student.student_id == student_id:
              self.students.remove(student)
              return True
      return False

def main():
  database = StudentDatabase()

  while True:
      
      print("-------CRUD WAGUINHO (LISTA DE ESTUDANTE)--------")

      print("\nEscolha uma opção:")
      print("1. Adicionar estudante")
      print("2. Listar estudantes")
      print("3. Atualizar estudante")
      print("4. Excluir estudante")
      print("5. Sair")

      choice = input("Digite o número da opção: ")

      if choice == '1':
          student_id = input("Digite o ID do estudante: ")
          nome = input("Digite o nome do estudante: ")
          idade = input("Digite a idade do estudante: ")
          mae = input("Digite o nome da mae: ")
          pai = input("Digite o nome do pai: ")
          database.create_student(student_id, nome, idade, mae, pai)
          print("Estudante adicionado com sucesso!")

      elif choice == '2':
          print("\nLista de Estudantes:")
          for student in database.students:
              print(f"ID: {student.student_id}, Nome: {student.nome}, Idade: {student.idade}, Mae: {student.mae}, Pai: {student.pai}")

      elif choice == '3':
          student_id = input("Digite o ID do estudante que deseja atualizar: ")
          name = input("Digite o novo nome do estudante: ")
          age = input("Digite a nova idade do estudante: ")
          mae = input("Digite o novo nome da mae: ")
          pai = input("Digite o novo nome do pai: ")
          if database.update_student(student_id, name, age, mae, pai):
              print("Estudante atualizado com sucesso!")
          else:
              print("Estudante não encontrado.")

      elif choice == '4':
          student_id = input("Digite o ID do estudante que deseja excluir: ")
          if database.delete_student(student_id):
              print("Estudante excluído com sucesso!")
          else:
              print("Estudante não encontrado.")

      elif choice == '5':
          print("Saindo do programa.")
          break

      else:
          print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()