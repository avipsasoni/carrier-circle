from threading import Thread
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from finalize.views import (
            AllIndiaGovernmentJobs,
            StatewiseGovtJobs,
            StatewiseTeachingJobs,
            StatewiseEngineeringJobs,
            RailwayJobs,
            BankingJobs,
            PoliceJobs
        )


class FinishAll:
    def all_india_govt_jobs(request):
        try:
            res = AllIndiaGovernmentJobs.call_all_india_govt_jobs(request)
            return HttpResponse("success")
        except:
            return HttpResponse("error")

    def state_govt_jobs(request):
        t1 = Thread(target=StatewiseGovtJobs.call_andaman_govt_jobs,args=[request])
        t2 = Thread(target=StatewiseGovtJobs.call_odisha_govt_jobs,args=[request])
        t3 = Thread(target=StatewiseGovtJobs.call_andhra_govt_jobs,args=[request])
        t4 = Thread(target=StatewiseGovtJobs.call_arunachal_pradesh_govt_jobs,args=[request])
        t5 = Thread(target=StatewiseGovtJobs.call_assam_govt_jobs,args=[request])
        t6 = Thread(target=StatewiseGovtJobs.call_bihar_govt_jobs,args=[request])
        t7 = Thread(target=StatewiseGovtJobs.call_chandigarh_govt_jobs,args=[request])
        t8 = Thread(target=StatewiseGovtJobs.call_chhattisgarh_govt_jobs,args=[request])
        t9 = Thread(target=StatewiseGovtJobs.call_dadra_nagar_govt_jobs,args=[request])
        t10 = Thread(target=StatewiseGovtJobs.call_daman_diu_govt_jobs,args=[request])
        t11 = Thread(target=StatewiseGovtJobs.call_delhi_govt_jobs,args=[request])
        t12 = Thread(target=StatewiseGovtJobs.call_goa_govt_jobs,args=[request])
        t13 = Thread(target=StatewiseGovtJobs.call_gujurat_govt_jobs,args=[request])
        t14 = Thread(target=StatewiseGovtJobs.call_haryana_govt_jobs,args=[request])
        t15 = Thread(target=StatewiseGovtJobs.call_himachal_pradesh_govt_jobs,args=[request])
        t16 = Thread(target=StatewiseGovtJobs.call_jammu_kashmir_govt_jobs,args=[request])
        t17 = Thread(target=StatewiseGovtJobs.call_jharkhand_govt_jobs,args=[request])
        t18 = Thread(target=StatewiseGovtJobs.call_karnataka_govt_jobs,args=[request])
        t19 = Thread(target=StatewiseGovtJobs.call_kerala_govt_jobs,args=[request])
        t20 = Thread(target=StatewiseGovtJobs.call_lakshadweep_govt_jobs,args=[request])
        t21 = Thread(target=StatewiseGovtJobs.call_madhya_pradesh_govt_jobs,args=[request])
        t22 = Thread(target=StatewiseGovtJobs.call_maharashtra_govt_jobs,args=[request])
        t23 = Thread(target=StatewiseGovtJobs.call_manipur_govt_jobs,args=[request])
        t24 = Thread(target=StatewiseGovtJobs.call_meghalaya_govt_jobs,args=[request])
        t25 = Thread(target=StatewiseGovtJobs.call_mizoram_govt_jobs,args=[request])
        t26 = Thread(target=StatewiseGovtJobs.call_nagaland_govt_jobs,args=[request])
        t27 = Thread(target=StatewiseGovtJobs.call_puduchhery_govt_jobs,args=[request])
        t28 = Thread(target=StatewiseGovtJobs.call_punjab_govt_jobs,args=[request])
        t29 = Thread(target=StatewiseGovtJobs.call_rajastan_govt_jobs,args=[request])
        t30 = Thread(target=StatewiseGovtJobs.call_sikkim_govt_jobs,args=[request])
        t31 = Thread(target=StatewiseGovtJobs.call_tamil_nadu_govt_jobs,args=[request])
        t32 = Thread(target=StatewiseGovtJobs.call_telengana_govt_jobs,args=[request])
        t33 = Thread(target=StatewiseGovtJobs.call_tripura_govt_jobs,args=[request])
        t34 = Thread(target=StatewiseGovtJobs.call_uttarakhand_govt_jobs,args=[request])
        t35 = Thread(target=StatewiseGovtJobs.call_uttar_pradesh_govt_jobs,args=[request])
        t36 = Thread(target=StatewiseGovtJobs.call_west_bengal_govt_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()

        return HttpResponse("success")

    def teaching_jobs(request):
        t1 = Thread(target=StatewiseTeachingJobs.call_andaman_teaching_jobs,args=[request])
        t2 = Thread(target=StatewiseTeachingJobs.call_odisha_teaching_jobs,args=[request])
        t3 = Thread(target=StatewiseTeachingJobs.call_andhra_teaching_jobs,args=[request])
        t4 = Thread(target=StatewiseTeachingJobs.call_arunachal_pradesh_teaching_jobs,args=[request])
        t5 = Thread(target=StatewiseTeachingJobs.call_assam_teaching_jobs,args=[request])
        t6 = Thread(target=StatewiseTeachingJobs.call_bihar_teaching_jobs,args=[request])
        t7 = Thread(target=StatewiseTeachingJobs.call_chandigarh_teaching_jobs,args=[request])
        t8 = Thread(target=StatewiseTeachingJobs.call_chhattisgarh_teaching_jobs,args=[request])
        t9 = Thread(target=StatewiseTeachingJobs.call_dadra_nagar_teaching_jobs,args=[request])
        t10 = Thread(target=StatewiseTeachingJobs.call_daman_diu_teaching_jobs,args=[request])
        t11 = Thread(target=StatewiseTeachingJobs.call_delhi_teaching_jobs,args=[request])
        t12 = Thread(target=StatewiseTeachingJobs.call_goa_teaching_jobs,args=[request])
        t13 = Thread(target=StatewiseTeachingJobs.call_gujurat_teaching_jobs,args=[request])
        t14 = Thread(target=StatewiseTeachingJobs.call_haryana_teaching_jobs,args=[request])
        t15 = Thread(target=StatewiseTeachingJobs.call_himachal_pradesh_teaching_jobs,args=[request])
        t16 = Thread(target=StatewiseTeachingJobs.call_jammu_kashmir_teaching_jobs,args=[request])
        t17 = Thread(target=StatewiseTeachingJobs.call_jharkhand_teaching_jobs,args=[request])
        t18 = Thread(target=StatewiseTeachingJobs.call_karnataka_teaching_jobs,args=[request])
        t19 = Thread(target=StatewiseTeachingJobs.call_kerala_teaching_jobs,args=[request])
        t20 = Thread(target=StatewiseTeachingJobs.call_lakshadweep_teaching_jobs,args=[request])
        t21 = Thread(target=StatewiseTeachingJobs.call_madhya_pradesh_teaching_jobs,args=[request])
        t22 = Thread(target=StatewiseTeachingJobs.call_maharashtra_teaching_jobs,args=[request])
        t23 = Thread(target=StatewiseTeachingJobs.call_manipur_teaching_jobs,args=[request])
        t24 = Thread(target=StatewiseTeachingJobs.call_meghalaya_teaching_jobs,args=[request])
        t25 = Thread(target=StatewiseTeachingJobs.call_mizoram_teaching_jobs,args=[request])
        t26 = Thread(target=StatewiseTeachingJobs.call_nagaland_teaching_jobs,args=[request])
        t27 = Thread(target=StatewiseTeachingJobs.call_puduchhery_teaching_jobs,args=[request])
        t28 = Thread(target=StatewiseTeachingJobs.call_punjab_teaching_jobs,args=[request])
        t29 = Thread(target=StatewiseTeachingJobs.call_rajastan_teaching_jobs,args=[request])
        t30 = Thread(target=StatewiseTeachingJobs.call_sikkim_teaching_jobs,args=[request])
        t31 = Thread(target=StatewiseTeachingJobs.call_tamil_nadu_teaching_jobs,args=[request])
        t32 = Thread(target=StatewiseTeachingJobs.call_telengana_teaching_jobs,args=[request])
        t33 = Thread(target=StatewiseTeachingJobs.call_tripura_teaching_jobs,args=[request])
        t34 = Thread(target=StatewiseTeachingJobs.call_uttarakhand_teaching_jobs,args=[request])
        t35 = Thread(target=StatewiseTeachingJobs.call_uttar_pradesh_teaching_jobs,args=[request])
        t36 = Thread(target=StatewiseTeachingJobs.call_west_bengal_teaching_jobs,args=[request])
        t37 = Thread(target=StatewiseTeachingJobs.call_all_india_teaching_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()
        t37.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()
        t37.join()

        return HttpResponse("success")

    def engineering_jobs(request):
        t1 = Thread(target=StatewiseEngineeringJobs.call_andaman_engg_jobs,args=[request])
        t2 = Thread(target=StatewiseEngineeringJobs.call_odisha_engg_jobs,args=[request])
        t3 = Thread(target=StatewiseEngineeringJobs.call_andhra_engg_jobs,args=[request])
        t4 = Thread(target=StatewiseEngineeringJobs.call_arunachal_pradesh_engg_jobs,args=[request])
        t5 = Thread(target=StatewiseEngineeringJobs.call_assam_engg_jobs,args=[request])
        t6 = Thread(target=StatewiseEngineeringJobs.call_bihar_engg_jobs,args=[request])
        t7 = Thread(target=StatewiseEngineeringJobs.call_chandigarh_engg_jobs,args=[request])
        t8 = Thread(target=StatewiseEngineeringJobs.call_chhattisgarh_engg_jobs,args=[request])
        t9 = Thread(target=StatewiseEngineeringJobs.call_dadra_nagar_engg_jobs,args=[request])
        t10 = Thread(target=StatewiseEngineeringJobs.call_daman_diu_engg_jobs,args=[request])
        t11 = Thread(target=StatewiseEngineeringJobs.call_delhi_engg_jobs,args=[request])
        t12 = Thread(target=StatewiseEngineeringJobs.call_goa_engg_jobs,args=[request])
        t13 = Thread(target=StatewiseEngineeringJobs.call_gujurat_engg_jobs,args=[request])
        t14 = Thread(target=StatewiseEngineeringJobs.call_haryana_engg_jobs,args=[request])
        t15 = Thread(target=StatewiseEngineeringJobs.call_himachal_pradesh_engg_jobs,args=[request])
        t16 = Thread(target=StatewiseEngineeringJobs.call_jammu_kashmir_engg_jobs,args=[request])
        t17 = Thread(target=StatewiseEngineeringJobs.call_jharkhand_engg_jobs,args=[request])
        t18 = Thread(target=StatewiseEngineeringJobs.call_karnataka_engg_jobs,args=[request])
        t19 = Thread(target=StatewiseEngineeringJobs.call_kerala_engg_jobs,args=[request])
        t20 = Thread(target=StatewiseEngineeringJobs.call_lakshadweep_engg_jobs,args=[request])
        t21 = Thread(target=StatewiseEngineeringJobs.call_madhya_pradesh_engg_jobs,args=[request])
        t22 = Thread(target=StatewiseEngineeringJobs.call_maharashtra_engg_jobs,args=[request])
        t23 = Thread(target=StatewiseEngineeringJobs.call_manipur_engg_jobs,args=[request])
        t24 = Thread(target=StatewiseEngineeringJobs.call_meghalaya_engg_jobs,args=[request])
        t25 = Thread(target=StatewiseEngineeringJobs.call_mizoram_engg_jobs,args=[request])
        t26 = Thread(target=StatewiseEngineeringJobs.call_nagaland_engg_jobs,args=[request])
        t27 = Thread(target=StatewiseEngineeringJobs.call_puduchhery_engg_jobs,args=[request])
        t28 = Thread(target=StatewiseEngineeringJobs.call_punjab_engg_jobs,args=[request])
        t29 = Thread(target=StatewiseEngineeringJobs.call_rajastan_engg_jobs,args=[request])
        t30 = Thread(target=StatewiseEngineeringJobs.call_sikkim_engg_jobs,args=[request])
        t31 = Thread(target=StatewiseEngineeringJobs.call_tamil_nadu_engg_jobs,args=[request])
        t32 = Thread(target=StatewiseEngineeringJobs.call_telengana_engg_jobs,args=[request])
        t33 = Thread(target=StatewiseEngineeringJobs.call_tripura_engg_jobs,args=[request])
        t34 = Thread(target=StatewiseEngineeringJobs.call_uttarakhand_engg_jobs,args=[request])
        t35 = Thread(target=StatewiseEngineeringJobs.call_uttar_pradesh_engg_jobs,args=[request])
        t36 = Thread(target=StatewiseEngineeringJobs.call_west_bengal_engg_jobs,args=[request])
        t37 = Thread(target=StatewiseEngineeringJobs.call_all_india_engg_jobs,args=[request])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()
        t25.start()
        t26.start()
        t27.start()
        t28.start()
        t29.start()
        t30.start()
        t31.start()
        t32.start()
        t33.start()
        t34.start()
        t35.start()
        t36.start()
        t37.start()


        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()
        t25.join()
        t26.join()
        t27.join()
        t28.join()
        t29.join()
        t30.join()
        t31.join()
        t32.join()
        t33.join()
        t34.join()
        t35.join()
        t36.join()
        t37.join()

        return HttpResponse("success")

    def banking_jobs(request):
        t1 = Thread(target=BankingJobs.call_all_bank_jobs,args=[request])
        t2 = Thread(target=BankingJobs.call_other_financial_jobs,args=[request])

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        return HttpResponse("success")

    def railway_jobs(request):
        res = RailwayJobs.call_railway_jobs(request)
        return HttpResponse("success")

    def police_jobs(request):
        t1 = Thread(target=PoliceJobs.call_police_defence_jobs,args=[request])
        t2 = Thread(target=PoliceJobs.call_statewise_police_jobs,args=[request])
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return HttpResponse("success")