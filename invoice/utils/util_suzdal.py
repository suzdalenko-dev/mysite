from decimal import Decimal
from django.http import JsonResponse
from invoice.models.article import Article
from invoice.models.company import Company
from invoice.models.customer import Customer
from invoice.models.document import Document
from copy import deepcopy


def json_suzdal(response_data):
    response = JsonResponse(response_data)

    # Set CORS headers
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
    return response



def user_auth(request):
    company_id = str(request.POST.get('company_id')).strip()
    cif        = str(request.POST.get('cif')).strip()
    email      = str(request.POST.get('email')).strip()
    uid        = str(request.POST.get('uid')).strip()
    password   = str(request.POST.get('password')).strip()

    try:
        company = Company.objects.filter(id=company_id).values('id', 'razon', 'cif', 'person_name', 'email', 'emailcompany', 'uid', 'password', 'tlf', 'tlf2', 'country', 'city', 'zipcode', 'province', 'address', 'price').first()
        if company['cif'] == cif and company['email'] == email and company['uid'] == uid and company['password'] == password:
            return [True, company]
        else: 
            return [None, None]
        
    except Exception as e:
        return [None, None]
    


def update_company_data(request):
    company_id = request.POST.get('company_id')
    try:
        c = Company.objects.get(id=company_id)
        c.razon        = str(request.POST.get('razon')).strip()
        c.person_name  = str(request.POST.get('person_name')).strip()
        c.emailcompany = str(request.POST.get('emailcompany')).strip()
        c.country      = str(request.POST.get('country')).strip()
        c.province     = str(request.POST.get('province')).strip()
        c.zipcode      = str(request.POST.get('zipcode')).strip()
        c.city         = str(request.POST.get('city')).strip()
        c.address      = str(request.POST.get('address')).strip()
        c.tlf          = str(request.POST.get('tlf')).strip()
        c.tlf2         = str(request.POST.get('tlf2')).strip()
        c.price        = str(request.POST.get('price')).strip().replace(',', '.')
        c.save()
        c = Company.objects.filter(id=company_id).values('id', 'razon', 'cif', 'person_name', 'email', 'emailcompany', 'uid', 'password', 'tlf', 'tlf2', 'country', 'city', 'zipcode', 'province', 'address', 'price').first()
        return [True, c]
    except Exception as e:
        print(str(e))
        return None



def create_new_article(request):
    description = str(request.POST.get('description')).strip()
    price       = str(request.POST.get('price')).replace(',', '.')
    iva         = str(request.POST.get('iva')).replace(',', '.')   
    ivatype     = str(request.POST.get('ivatype')).strip()
    company_id  = int(request.POST.get('company_id'))
    article     = None
    try:
        article  = Article.objects.create(description=description, company_id=company_id, price=price, ivatype=ivatype, iva=iva)   
        document = Document.objects.filter(company_id=company_id, description= 'articulo_numero').values('value').first() 
        article.artcode = document['value']
        article.save()
        if article.id > 0:
            return True
        else:
            return None
    except Exception as e:
        if article is not None:
            article.delete()
        return None
    


def create_new_customer(request):
    company_id    = int(request.POST.get('company_id'))
    cif_nif       = str(request.POST.get('cif_nif')).strip()
    razon         = str(request.POST.get('razon')).strip()
    person_name   = str(request.POST.get('person_name')).strip()
    emailcustomer = str(request.POST.get('emailcustomer')).strip()
    phone         = str(request.POST.get('phone')).strip()
    country       = str(request.POST.get('country')).strip()
    province      = str(request.POST.get('province')).strip()
    zipcode       = str(request.POST.get('zipcode')).strip()
    city          = str(request.POST.get('city')).strip()
    address       = str(request.POST.get('address')).strip()
    customer      = None
    try:
        customer = Customer.objects.create(cif_nif=cif_nif, company_id=company_id, razon=razon, person_name=person_name, emailcustomer=emailcustomer, phone=phone, country=country, province=province, zipcode=zipcode, city=city, address=address)
        document = Document.objects.filter(company_id=company_id, description= 'cliente_numero').values('value').first()
        customer.clientcode = document['value']
        customer.save()
        if customer.id > 0:
            return True
        else:
            return None
    except Exception as e:
        customer.delete()
        return None
    

def upgrade_existing_customer(request, id):
    company_id    = int(request.POST.get('company_id'))
    try:
        customer               = Customer.objects.get(id=id, company_id=company_id)
        customer.cif_nif       = str(request.POST.get('cif_nif')).strip()
        customer.razon         = str(request.POST.get('razon')).strip()
        customer.person_name   = str(request.POST.get('person_name')).strip()
        customer.emailcustomer = str(request.POST.get('emailcustomer')).strip()
        customer.phone         = str(request.POST.get('phone')).strip()
        customer.country       = str(request.POST.get('country')).strip()
        customer.province      = str(request.POST.get('province')).strip()
        customer.zipcode       = str(request.POST.get('zipcode')).strip()
        customer.city          = str(request.POST.get('city')).strip()
        customer.address       = str(request.POST.get('address')).strip()
        customer.save()
        if customer.id > 0:
            return True
        else:
            return None
    except Exception as e:
        return None
    


def update_old_article(request, id):
    company_id  = int(request.POST.get('company_id'))
    try:
        article  = Article.objects.get(id=id, company_id=company_id)   
        article.description = str(request.POST.get('description')).strip()
        article.price       = str(request.POST.get('price')).replace(',', '.')
        article.iva         = str(request.POST.get('iva')).replace(',', '.')   
        article.ivatype     = str(request.POST.get('ivatype')).strip()
        article.save()
        if article.id > 0:
            return True
        else:
            return None
    except Exception as e:
        return None