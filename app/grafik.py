from django.views import generic
from django.http import JsonResponse
from app import models


class AnggotaByDevisi(generic.View):
    def get(self, request):
        data = list()
        kategori = models.Devisi.objects.all()
        for devisi in kategori:
            anggota = models.Anggota.objects\
                .filter(
                    devisi_id=devisi
                )

            data.append(
                {
                    "y": anggota.count() \
                        if anggota.exists() else 0,
                    "name": devisi.devisi,
                }
            )

        data_response = {
            "name": 'Brands',
            "colorByPoint": True,
            "data": data
        }
        return JsonResponse(data_response)