from django.http.response import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy


@csrf_exempt
def company_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })
    return JsonResponse(company.to_json())



def company_vacancy(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        vacancies = Vacancy.objects.filter(company=company)
        data = {
            'company': company.to_json(),
            'vacancies': [vacancy().to_json() for vacancy in vacancies],
        }
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })
    return JsonResponse(data)
