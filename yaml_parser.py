import yaml

# Define un cargador personalizado
class CustomLoader(yaml.SafeLoader):
    pass

# Constructor para manejar !GetAtt
def getatt_constructor(loader, node):
    # Devuelve el contenido como lista
    return loader.construct_sequence(node)

# Constructor para manejar !Ref
def ref_constructor(loader, node):
    # Devuelve el contenido como string
    return loader.construct_scalar(node)

# Registra los constructores solo para el cargador personalizado
CustomLoader.add_constructor('!GetAtt', getatt_constructor)
CustomLoader.add_constructor('!Ref', ref_constructor)

# Ejemplo de YAML con etiquetas personalizadas
yaml_string = """
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      KeyName: !Ref MyKeyPair
      SubnetId: !GetAtt [ MySubnet, SubnetId ]
"""

# Cargar el YAML usando el cargador personalizado
parsed_data = yaml.load(yaml_string, Loader=CustomLoader)
print(parsed_data)
