from django.urls import path
from scrap.views import (
                AllIndiaGovtJobs,
                StateGovtJobs,
                BankJobs,
                TeachingJobs,
                EnggJobs,
                RailwayJobs,
                PoliceDefenceJobs
            )

urlpatterns = [
    #All India Govt Jobs
    path('upsc/', AllIndiaGovtJobs.get_upsc),
    path('ssc/', AllIndiaGovtJobs.get_ssc),
    path('other_all_india/', AllIndiaGovtJobs.get_other_all_india),
    # State Wise Govt Jobs
    path('odisha_govt_jobs/', StateGovtJobs.odisha_govt_jobs),
    path('andaman_nicobor_govt_jobs/', StateGovtJobs.andaman_nicobor_govt_jobs),
    path('andhra_prtadesh_govt_jobs/', StateGovtJobs.andhra_prtadesh_govt_jobs),
    path('arunachal_pradesh_government_jobs/', StateGovtJobs.arunachal_pradesh_government_jobs),
    path('assam_govt_jobs/', StateGovtJobs.assam_govt_jobs),
    path('bihar_govt_jobs/', StateGovtJobs.bihar_govt_jobs),
    path('chandigarh_govt_jobs/', StateGovtJobs.chandigarh_govt_jobs),
    path('chhattisgarh_govt_jobs/', StateGovtJobs.chhattisgarh_govt_jobs),
    path('dadra_nagar_haveli_govt_jobs/', StateGovtJobs.dadra_nagar_haveli_govt_jobs),
    path('daman_diu_govt_jobs/', StateGovtJobs.daman_diu_govt_jobs),
    path('delhi_govt_jobs/', StateGovtJobs.delhi_govt_jobs),
    path('goa_govt_jobs/', StateGovtJobs.goa_govt_jobs),
    path('gujurat_govt_jobs/', StateGovtJobs.gujurat_govt_jobs),
    path('haryana_govt_jobs/', StateGovtJobs.haryana_govt_jobs),
    path('himachal_pradesh_govt_jobs/', StateGovtJobs.himachal_pradesh_govt_jobs),
    path('jammu_kashmir_govt_jobs/', StateGovtJobs.jammu_kashmir_govt_jobs),
    path('jharkhand_govt_jobs/', StateGovtJobs.jharkhand_govt_jobs),
    path('karnataka_govt_jobs/', StateGovtJobs.karnataka_govt_jobs),
    path('kerala_govt_jobs/', StateGovtJobs.kerala_govt_jobs),
    path('lakshadweep_govt_jobs/', StateGovtJobs.lakshadweep_govt_jobs),
    path('madhya_pradesh_govt_jobs/', StateGovtJobs.madhya_pradesh_govt_jobs),
    path('maharashtra_govt_jobs/', StateGovtJobs.maharashtra_govt_jobs),
    path('manipur_govt_jobs/', StateGovtJobs.manipur_govt_jobs),
    path('meghalaya_govt_jobs/', StateGovtJobs.meghalaya_govt_jobs),
    path('mizoram_govt_jobs/', StateGovtJobs.mizoram_govt_jobs),
    path('nagaland_govt_jobs/', StateGovtJobs.nagaland_govt_jobs),
    path('puduchhery_govt_jobs/', StateGovtJobs.puduchhery_govt_jobs),
    path('punjab_govt_jobs/', StateGovtJobs.punjab_govt_jobs),
    path('rajasthan_govt_jobs/', StateGovtJobs.rajasthan_govt_jobs),
    path('sikkim_govt_jobs/', StateGovtJobs.sikkim_govt_jobs),
    path('tamil_nadu_govt_jobs/', StateGovtJobs.tamil_nadu_govt_jobs),
    path('telangana_govt_jobs/', StateGovtJobs.telangana_govt_jobs),
    path('tripura_govt_jobs/', StateGovtJobs.tripura_govt_jobs),
    path('uttarakhand_govt_jobs/', StateGovtJobs.uttarakhand_govt_jobs),
    path('uttar_pradesh_govt_jobs/', StateGovtJobs.uttar_pradesh_govt_jobs),
    path('west_bengal_govt_jobs/', StateGovtJobs.west_bengal_govt_jobs),
    #Bank Jobs
    path('all_bank_jobs/', BankJobs.all_bank_jobs),
    path('other_financial_jobs/', BankJobs.other_financial_jobs),
    #Teaching Jobs
    path('all_india_teaching_jobs/', TeachingJobs.all_india_teaching_jobs),
    path('andaman_nicobar_teaching_jobs/', TeachingJobs.andaman_nicobar_teaching_jobs),
    path('andhra_pradesh_teaching_jobs/', TeachingJobs.andhra_pradesh_teaching_jobs),
    path('arunachal_pradesh_teaching_jobs/', TeachingJobs.arunachal_pradesh_teaching_jobs),
    path('assam_teaching_jobs/', TeachingJobs.assam_teaching_jobs),
    path('bihar_teaching_jobs/', TeachingJobs.bihar_teaching_jobs),
    path('chandigarh_teaching_jobs/', TeachingJobs.chandigarh_teaching_jobs),
    path('chhattisgarh_teaching_jobs/', TeachingJobs.chhattisgarh_teaching_jobs),
    path('dadra_nagar_haveli_teaching_jobs/', TeachingJobs.dadra_nagar_haveli_teaching_jobs),
    path('daman_diu_teaching_jobs/', TeachingJobs.daman_diu_teaching_jobs),
    path('delhi_teaching_jobs/', TeachingJobs.delhi_teaching_jobs),
    path('goa_teaching_jobs/', TeachingJobs.goa_teaching_jobs),
    path('gujurat_teaching_jobs/', TeachingJobs.gujurat_teaching_jobs),
    path('haryana_teaching_jobs/', TeachingJobs.haryana_teaching_jobs),
    path('himachal_pradesh_teaching_jobs/', TeachingJobs.himachal_pradesh_teaching_jobs),
    path('jammu_kashmir_teaching_jobs/', TeachingJobs.jammu_kashmir_teaching_jobs),
    path('jharkhand_teaching_jobs/', TeachingJobs.jharkhand_teaching_jobs),
    path('karnataka_teaching_jobs/', TeachingJobs.karnataka_teaching_jobs),
    path('kerala_teaching_jobs/', TeachingJobs.kerala_teaching_jobs),
    path('lakshadweep_teaching_jobs/', TeachingJobs.lakshadweep_teaching_jobs),
    path('madhya_pradesh_teaching_jobs/', TeachingJobs.madhya_pradesh_teaching_jobs),
    path('maharashtra_teaching_jobs/', TeachingJobs.maharashtra_teaching_jobs),
    path('manipur_teaching_jobs/', TeachingJobs.manipur_teaching_jobs),
    path('meghalaya_teaching_jobs/', TeachingJobs.meghalaya_teaching_jobs),
    path('mizoram_teaching_jobs/', TeachingJobs.mizoram_teaching_jobs),
    path('nagaland_teaching_jobs/', TeachingJobs.nagaland_teaching_jobs),
    path('odisha_teaching_jobs/', TeachingJobs.odisha_teaching_jobs),
    path('puduchhery_teaching_jobs/', TeachingJobs.puduchhery_teaching_jobs),
    path('punjab_teaching_jobs/', TeachingJobs.punjab_teaching_jobs),
    path('rajasthan_teaching_jobs/', TeachingJobs.rajasthan_teaching_jobs),
    path('sikkim_teaching_jobs/', TeachingJobs.sikkim_teaching_jobs),
    path('tamil_nadu_teaching_jobs/', TeachingJobs.tamil_nadu_teaching_jobs),
    path('telangana_teaching_jobs/', TeachingJobs.telangana_teaching_jobs),
    path('tripura_teaching_jobs/', TeachingJobs.tripura_teaching_jobs),
    path('uttarakhand_teaching_jobs/', TeachingJobs.uttarakhand_teaching_jobs),
    path('uttar_pradesh_teaching_jobs/', TeachingJobs.uttar_pradesh_teaching_jobs),
    path('west_bengal_teaching_jobs/', TeachingJobs.west_bengal_teaching_jobs),
    #Engineering Jobs
    path('all_india_engg_jobs/', EnggJobs.all_india_engg_jobs),
    path('all_india_fellow_engg_jobs/', EnggJobs.all_india_fellow_engg_jobs),
    path('andaman_nicobar_engg_jobs/', EnggJobs.andaman_nicobar_engg_jobs),
    path('andhra_pradesh_engg_jobs/', EnggJobs.andhra_pradesh_engg_jobs),
    path('arunachal_pradesh_engg_jobs/', EnggJobs.arunachal_pradesh_engg_jobs),
    path('assam_engg_jobs/', EnggJobs.assam_engg_jobs),
    path('bihar_engg_jobs/', EnggJobs.bihar_engg_jobs),
    path('chandigarh_engg_jobs/', EnggJobs.chandigarh_engg_jobs),
    path('chhattisgarh_engg_jobs/', EnggJobs.chhattisgarh_engg_jobs),
    path('dadra_nagar_haveli_engg_jobs/', EnggJobs.dadra_nagar_haveli_engg_jobs),
    path('daman_diu_engg_jobs/', EnggJobs.daman_diu_engg_jobs),
    path('delhi_engg_jobs/', EnggJobs.delhi_engg_jobs),
    path('goa_engg_jobs/', EnggJobs.goa_engg_jobs),
    path('gujurat_engg_jobs/', EnggJobs.gujurat_engg_jobs),
    path('haryana_engg_jobs/', EnggJobs.haryana_engg_jobs),
    path('himachal_pradesh_engg_jobs/', EnggJobs.himachal_pradesh_engg_jobs),
    path('jammu_kashmir_engg_jobs/', EnggJobs.jammu_kashmir_engg_jobs),
    path('jharkhand_engg_jobs/', EnggJobs.jharkhand_engg_jobs),
    path('karnataka_engg_jobs/', EnggJobs.karnataka_engg_jobs),
    path('kerala_engg_jobs/', EnggJobs.kerala_engg_jobs),
    path('lakshadweep_engg_jobs/', EnggJobs.lakshadweep_engg_jobs),
    path('madhya_pradesh_engg_jobs/', EnggJobs.madhya_pradesh_engg_jobs),
    path('maharashtra_engg_jobs/', EnggJobs.maharashtra_engg_jobs),
    path('manipur_engg_jobs/', EnggJobs.manipur_engg_jobs),
    path('meghalaya_engg_jobs/', EnggJobs.meghalaya_engg_jobs),
    path('mizoram_engg_jobs/', EnggJobs.mizoram_engg_jobs),
    path('nagaland_engg_jobs/', EnggJobs.nagaland_engg_jobs),
    path('odisha_engg_jobs/', EnggJobs.odisha_engg_jobs),
    path('puduchhery_engg_jobs/', EnggJobs.puduchhery_engg_jobs),
    path('punjab_engg_jobs/', EnggJobs.punjab_engg_jobs),
    path('rajasthan_engg_jobs/', EnggJobs.rajasthan_engg_jobs),
    path('sikkim_engg_jobs/', EnggJobs.sikkim_engg_jobs),
    path('tamil_nadu_engg_jobs/', EnggJobs.tamil_nadu_engg_jobs),
    path('telangana_engg_jobs/', EnggJobs.telangana_engg_jobs),
    path('tripura_engg_jobs/', EnggJobs.tripura_engg_jobs),
    path('uttarakhand_engg_jobs/', EnggJobs.uttarakhand_engg_jobs),
    path('uttar_pradesh_engg_jobs/', EnggJobs.uttar_pradesh_engg_jobs),
    path('west_bengal_engg_jobs/', EnggJobs.west_bengal_engg_jobs),
    #Railway Jobs
    path('railway_jobs/', RailwayJobs.railway_jobs),
    #Police and Defence Jobs
    path('police_defence_jobs/', PoliceDefenceJobs.police_defence_jobs),
    path('statewise_police_jobs/', PoliceDefenceJobs.statewise_police_jobs),

]
