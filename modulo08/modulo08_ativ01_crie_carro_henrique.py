# esse código cria uma classe chamada Carro com atributos de marca e modelo e um método para exibir essas informações.
class Carro:
    
    def __init__(self,marca, modelo):
        self.marca = marca 
        self.modelo = modelo
        
    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
        
meu_carro = Carro("Chevtrolet", "Camaro")
print(meu_carro.exibir_info())