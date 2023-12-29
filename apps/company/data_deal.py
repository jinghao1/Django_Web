from .models import Result,Desc


def Result_maker(result_info):


    info = Result.objects.filter(
        xn_href=result_info['xn_href']).exists()
    if info:
        Result.objects.filter(xn_href=result_info['xn_href']).update(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            search_name=result_info['search_name'],
        )
        return "update"
    else:
        res = Result.objects.create(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            xn_href=result_info['xn_href'],
            search_name=result_info['search_name'],
        )
        return "insert"

def Desc_maker(com_info={}):
    # com_info = cont["props"]["pageProps"]["company"]

    Desc.objects.update_or_create(defaults={
        "name":com_info["name"],
        "brief":com_info["brief"],
        "roundName":com_info["roundName"],
        "cityName":com_info["cityName"] + ">" + com_info["districtName"],
        "establishDate":com_info["establishDate"],
    },xn_href=result_info['xn_href'])



def GongShang_maker(result_info):


    info = Desc.objects.filter(
        xn_href=result_info['xn_href']).exists()
    if info:
        Desc.objects.filter(xn_href=result_info['xn_href']).update(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            search_name=result_info['search_name'],
        )
        return "update"
    else:
        res = Desc.objects.create(
            title=result_info['title'],
            brief=result_info['brief'],
            highlight=result_info['highlight'],
            xn_href=result_info['xn_href'],
            search_name=result_info['search_name'],
        )
        return "insert"