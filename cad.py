import pycep_correios

endereco = pycep_correios.get_address_from_cep('21842600')
print(endereco)


class CLiente:
    def Endereco(self, cep=0, Log=0, num=0, bairro=0, cidade=0, estado=0):
        '''
        :param cep: CEP do endereço
        :param Log: Logradouro
        :param num: Número do endereço
        :param bairro: Bairro
        :param cidade: Cidade
        :param estado: Estado
        :return:
        '''
        cep = input('CEP: ')
        num = input('Número: ')
        Log = endereco['logradouro']
        bairro = endereco['bairro']
        cidade = endereco['cidade']
        end = {'cep': cep, 'num': num, 'Log': Log, 'bairro': bairro, 'cidade': cidade}
        return end

    def dados(self, nome=0, email=0, doc=0, tel=0):
        '''
        :param nome: Nome do Cliente
        :param email: Endereço de email do cliente
        :param doc: Documento do cliente, CPF ou CNPJ
        :param tel: Telefone do Cliente
        :return: retorna os dados
        '''
        nome = input('Nome completo: ')
        doc = input('CPF/CNPJ: ')
        email = input('Endereço de e-mail: ')
        tel = input('Telefone: ')
        return {'nome': nome, 'doc': doc, 'email': email, 'tel': tel}
