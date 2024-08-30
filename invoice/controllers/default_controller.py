from invoice.models.company import Company
from invoice.models.factura import Factura
from invoice.models.customer import Customer
from invoice.models.article import Article
from ..utils.util_suzdal import json_suzdal, user_auth


def default_actions(request, action, entity, id):
    auth_status, company = user_auth(request)
    if auth_status is None or company is None:
        return json_suzdal({'login': False})

    try:
        response = []

        if action == 'get' and entity == 'factura':
            facturas = Factura.objects.filter(company_id=company['id']).order_by('-id').values('id', 'numero', 'fecha', 'nombre_cliente', 'total')
            for factura in facturas:
                x = {'id':factura['id'], 'numero':factura['numero'], 'fecha':factura['fecha'],'nombre':factura['nombre_cliente'], 'total': factura['total'] }
                response += [x]
            return json_suzdal({'res':response, 'status':'ok', 'company':company})


        elif action == 'get' and entity == 'cliente':
            clientes = Customer.objects.filter(company_id=company['id']).order_by('-id').values('id', 'name')
            for cliente in clientes:
                x = {'id':cliente['id'], 'name':cliente['name'], }
                response += [x]
            return json_suzdal({'res':response, 'status':'ok', 'company':company})


        elif action == 'get' and entity == 'articulo':
            articulos = Article.objects.filter(company_id=company['id']).order_by('-id').values('id', 'description')
            for articulo in articulos:
                x = {'id':articulo['id'], 'description':articulo['description'], }
                response += [x]
            return json_suzdal({'res':response, 'status':'ok'})

        else:
            return json_suzdal({'message': 'Invalid action or entity', 'status': 'error', 'company':company})

    
    except Exception as e:
        return json_suzdal({'message': str(e),'status': 'error'})
  