from django.shortcuts import render
from details.views import *
from scrap.views import *
from django.http import HttpResponse
from queue import Queue
import threading
from time import sleep
from finalize.utils import HandleError

def call_all(job,job_details):
    try:
        if job.status_code and job_details.status_code == 200:
            return "success"
        elif job_details["code"] or job["code"] == 402:
            if job_details["code"] == 402:
                return job_details["traceback"]
            if job["code"]         == 402:
                return job["traceback"]
        else:
            return "Unknown error happened"
    except AttributeError:
        try:
            return job_details["traceback"]
        except KeyError:
            return job["traceback"]

class AllIndiaGovernmentJobs:
    def call_all_india_govt_jobs(request):
        try:
            job         = AllIndiaGovtJobs.get_other_all_india(request)
            print(AllIndiaGovtJobs)
            sleep(0.5)
            job_details = AllIndiaGovtJobDetails.other_all_india_details(request)
            print(AllIndiaGovtJobDetails)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class StatewiseGovtJobs:

    def call_andaman_govt_jobs(request):
        try:
            job         = StateGovtJobs.andaman_nicobor_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.andaman_nicobar_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_odisha_govt_jobs(request):
        try:
            job         = StateGovtJobs.odisha_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.odisha_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_andhra_govt_jobs(request):
        try:
            job         = StateGovtJobs.andhra_prtadesh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.andhra_pradesh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_arunachal_pradesh_govt_jobs(request):
        try:
            job         = StateGovtJobs.arunachal_pradesh_government_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.arunachal_pradesh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_assam_govt_jobs(request):
        try:
            job         = StateGovtJobs.assam_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.assam_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_bihar_govt_jobs(request):
        try:
            job         = StateGovtJobs.bihar_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.bihar_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chandigarh_govt_jobs(request):
        try:
            job         = StateGovtJobs.chandigarh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.chandigarh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chhattisgarh_govt_jobs(request):
        try:
            job         = StateGovtJobs.chhattisgarh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.chhattisgarh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_dadra_nagar_govt_jobs(request):
        try:
            job         = StateGovtJobs.dadra_nagar_haveli_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.dadra_nagar_haveli_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_daman_diu_govt_jobs(request):
        try:
            job         = StateGovtJobs.daman_diu_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.daman_diu_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_delhi_govt_jobs(request):
        try:
            job         = StateGovtJobs.delhi_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.delhi_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_goa_govt_jobs(request):
        try:
            job         = StateGovtJobs.goa_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.goa_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_gujurat_govt_jobs(request):
        try:
            job         = StateGovtJobs.gujurat_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.gujurat_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_haryana_govt_jobs(request):
        try:
            job         = StateGovtJobs.haryana_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.haryana_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_himachal_pradesh_govt_jobs(request):
        try:
            job         = StateGovtJobs.himachal_pradesh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.himachal_pradesh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jammu_kashmir_govt_jobs(request):
        try:
            job         = StateGovtJobs.jammu_kashmir_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.jammu_kashmir_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jharkhand_govt_jobs(request):
        try:
            job         = StateGovtJobs.jharkhand_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.jharkhand_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_karnataka_govt_jobs(request):
        try:
            job         = StateGovtJobs.karnataka_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.karnataka_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_kerala_govt_jobs(request):
        try:
            job         = StateGovtJobs.kerala_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.kerala_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_lakshadweep_govt_jobs(request):
        try:
            job         = StateGovtJobs.lakshadweep_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.lakshadweep_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_madhya_pradesh_govt_jobs(request):
        try:
            job         = StateGovtJobs.madhya_pradesh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.madhya_pradesh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_maharashtra_govt_jobs(request):
        try:
            job         = StateGovtJobs.maharashtra_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.maharashtra_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_manipur_govt_jobs(request):
        try:
            job         = StateGovtJobs.manipur_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.manipur_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_meghalaya_govt_jobs(request):
        try:
            job         = StateGovtJobs.meghalaya_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.meghalaya_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_mizoram_govt_jobs(request):
        try:
            job         = StateGovtJobs.mizoram_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.mizoram_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_nagaland_govt_jobs(request):
        try:
            job         = StateGovtJobs.nagaland_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.nagaland_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_puduchhery_govt_jobs(request):
        try:
            job         = StateGovtJobs.puduchhery_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.puduchhery_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_punjab_govt_jobs(request):
        try:
            job         = StateGovtJobs.punjab_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.punjab_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_rajastan_govt_jobs(request):
        try:
            job         = StateGovtJobs.rajasthan_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.rajasthan_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_sikkim_govt_jobs(request):
        try:
            job         = StateGovtJobs.sikkim_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.sikkim_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tamil_nadu_govt_jobs(request):
        try:
            job         = StateGovtJobs.tamil_nadu_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.tamil_nadu_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_telengana_govt_jobs(request):
        try:
            job         = StateGovtJobs.telangana_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.telangana_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tripura_govt_jobs(request):
        try:
            job         = StateGovtJobs.tripura_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.tripura_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttarakhand_govt_jobs(request):
        try:
            job         = StateGovtJobs.uttarakhand_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.uttarakhand_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttar_pradesh_govt_jobs(request):
        try:
            job         = StateGovtJobs.uttar_pradesh_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.uttar_pradesh_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_west_bengal_govt_jobs(request):
        try:
            job         = StateGovtJobs.west_bengal_govt_jobs(request)
            sleep(0.5)
            job_details = StateGovtJobDetails.west_bengal_govt_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class BankingJobs:
    def call_all_bank_jobs(request):
        try:
            job         = BankJobs.all_bank_jobs(request)
            sleep(0.5)
            job_details = BankJobDetails.all_bank_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_other_financial_jobs(request):
        try:
            job         = BankJobs.other_financial_jobs(request)
            sleep(0.5)
            job_details = BankJobDetails.other_financial_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class StatewiseTeachingJobs:
    def call_all_india_teaching_jobs(request):
        try:
            job         = TeachingJobs.all_india_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.all_india_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_andaman_teaching_jobs(request):
        try:
            job         = TeachingJobs.andaman_nicobar_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.andaman_nicobar_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_odisha_teaching_jobs(request):
        try:
            job         = TeachingJobs.odisha_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.odisha_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_andhra_teaching_jobs(request):
        try:
            job         = TeachingJobs.andhra_pradesh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.andhra_pradesh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_arunachal_pradesh_teaching_jobs(request):
        try:
            job         = TeachingJobs.arunachal_pradesh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.arunachal_pradesh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_assam_teaching_jobs(request):
        try:
            job         = TeachingJobs.assam_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.assam_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_bihar_teaching_jobs(request):
        try:
            job         = TeachingJobs.bihar_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.bihar_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chandigarh_teaching_jobs(request):
        try:
            job         = TeachingJobs.chandigarh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.chandigarh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chhattisgarh_teaching_jobs(request):
        try:
            job         = TeachingJobs.chhattisgarh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.chhattisgarh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_dadra_nagar_teaching_jobs(request):
        try:
            job         = TeachingJobs.dadra_nagar_haveli_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.dadra_nagar_haveli_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_daman_diu_teaching_jobs(request):
        try:
            job         = TeachingJobs.daman_diu_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.daman_diu_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_delhi_teaching_jobs(request):
        try:
            job         = TeachingJobs.delhi_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.delhi_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_goa_teaching_jobs(request):
        try:
            job         = TeachingJobs.goa_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.goa_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_gujurat_teaching_jobs(request):
        try:
            job         = TeachingJobs.gujurat_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.gujurat_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_haryana_teaching_jobs(request):
        try:
            job         = TeachingJobs.haryana_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.haryana_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_himachal_pradesh_teaching_jobs(request):
        try:
            job         = TeachingJobs.himachal_pradesh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.himachal_pradesh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jammu_kashmir_teaching_jobs(request):
        try:
            job         = TeachingJobs.jammu_kashmir_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.jammu_kashmir_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jharkhand_teaching_jobs(request):
        try:
            job         = TeachingJobs.jharkhand_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.jharkhand_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_karnataka_teaching_jobs(request):
        try:
            job         = TeachingJobs.karnataka_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.karnataka_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_kerala_teaching_jobs(request):
        try:
            job         = TeachingJobs.kerala_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.kerala_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_lakshadweep_teaching_jobs(request):
        try:
            job         = TeachingJobs.lakshadweep_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.lakshadweep_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_madhya_pradesh_teaching_jobs(request):
        try:
            job         = TeachingJobs.madhya_pradesh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.madhya_pradesh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_maharashtra_teaching_jobs(request):
        try:
            job         = TeachingJobs.maharashtra_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.maharashtra_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_manipur_teaching_jobs(request):
        try:
            job         = TeachingJobs.manipur_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.manipur_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_meghalaya_teaching_jobs(request):
        try:
            job         = TeachingJobs.meghalaya_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.meghalaya_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_mizoram_teaching_jobs(request):
        try:
            job         = TeachingJobs.mizoram_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.mizoram_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_nagaland_teaching_jobs(request):
        try:
            job         = TeachingJobs.nagaland_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.nagaland_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_puduchhery_teaching_jobs(request):
        try:
            job         = TeachingJobs.puduchhery_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.puduchhery_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_punjab_teaching_jobs(request):
        try:
            job         = TeachingJobs.punjab_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.punjab_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_rajastan_teaching_jobs(request):
        try:
            job         = TeachingJobs.rajasthan_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.rajasthan_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_sikkim_teaching_jobs(request):
        try:
            job         = TeachingJobs.sikkim_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.sikkim_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tamil_nadu_teaching_jobs(request):
        try:
            job         = TeachingJobs.tamil_nadu_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.tamil_nadu_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_telengana_teaching_jobs(request):
        try:
            job         = TeachingJobs.telangana_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.telangana_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tripura_teaching_jobs(request):
        try:
            job         = TeachingJobs.tripura_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.tripura_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttarakhand_teaching_jobs(request):
        try:
            job         = TeachingJobs.uttarakhand_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.uttarakhand_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttar_pradesh_teaching_jobs(request):
        try:
            job         = TeachingJobs.uttar_pradesh_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.uttar_pradesh_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_west_bengal_teaching_jobs(request):
        try:
            job         = TeachingJobs.west_bengal_teaching_jobs(request)
            sleep(0.5)
            job_details = TeachingJobDetails.west_bengal_teaching_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class StatewiseEngineeringJobs:
    def call_all_india_engg_jobs(request):
        try:
            job         = EnggJobs.all_india_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.all_india_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_all_india_fellow_engg_jobs(request):
        try:
            job         = EnggJobs.all_india_fellow_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.all_india_fellow_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_andaman_engg_jobs(request):
        try:
            job         = EnggJobs.andaman_nicobar_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.andaman_nicobar_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_odisha_engg_jobs(request):
        try:
            job         = EnggJobs.odisha_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.odisha_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_andhra_engg_jobs(request):
        try:
            job         = EnggJobs.andhra_pradesh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.andhra_pradesh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors
    def call_arunachal_pradesh_engg_jobs(request):
        try:
            job         = EnggJobs.arunachal_pradesh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.arunachal_pradesh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_assam_engg_jobs(request):
        try:
            job         = EnggJobs.assam_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.assam_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_bihar_engg_jobs(request):
        try:
            job         = EnggJobs.bihar_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.bihar_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chandigarh_engg_jobs(request):
        try:
            job         = EnggJobs.chandigarh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.chandigarh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_chhattisgarh_engg_jobs(request):
        try:
            job         = EnggJobs.chhattisgarh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.chhattisgarh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_dadra_nagar_engg_jobs(request):
        try:
            job         = EnggJobs.dadra_nagar_haveli_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.dadra_nagar_haveli_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_daman_diu_engg_jobs(request):
        try:
            job         = EnggJobs.daman_diu_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.daman_diu_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_delhi_engg_jobs(request):
        try:
            job         = EnggJobs.delhi_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.delhi_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_goa_engg_jobs(request):
        try:
            job         = EnggJobs.goa_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.goa_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_gujurat_engg_jobs(request):
        try:
            job         = EnggJobs.gujurat_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.gujurat_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_haryana_engg_jobs(request):
        try:
            job         = EnggJobs.haryana_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.haryana_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_himachal_pradesh_engg_jobs(request):
        try:
            job         = EnggJobs.himachal_pradesh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.himachal_pradesh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jammu_kashmir_engg_jobs(request):
        try:
            job         = EnggJobs.jammu_kashmir_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.jammu_kashmir_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_jharkhand_engg_jobs(request):
        try:
            job         = EnggJobs.jharkhand_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.jharkhand_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors
    def call_karnataka_engg_jobs(request):
        try:
            job         = EnggJobs.karnataka_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.karnataka_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_kerala_engg_jobs(request):
        try:
            job         = EnggJobs.kerala_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.kerala_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_lakshadweep_engg_jobs(request):
        try:
            job         = EnggJobs.lakshadweep_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.lakshadweep_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_madhya_pradesh_engg_jobs(request):
        try:
            job         = EnggJobs.madhya_pradesh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.madhya_pradesh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_maharashtra_engg_jobs(request):
        try:
            job         = EnggJobs.maharashtra_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.maharashtra_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_manipur_engg_jobs(request):
        try:
            job         = EnggJobs.manipur_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.manipur_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_meghalaya_engg_jobs(request):
        try:
            job         = EnggJobs.meghalaya_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.meghalaya_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_mizoram_engg_jobs(request):
        try:
            job         = EnggJobs.mizoram_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.mizoram_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_nagaland_engg_jobs(request):
        try:
            job         = EnggJobs.nagaland_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.nagaland_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_puduchhery_engg_jobs(request):
        try:
            job         = EnggJobs.puduchhery_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.puduchhery_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_punjab_engg_jobs(request):
        try:
            job         = EnggJobs.punjab_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.punjab_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_rajastan_engg_jobs(request):
        try:
            job         = EnggJobs.rajasthan_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.rajasthan_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_sikkim_engg_jobs(request):
        try:
            job         = EnggJobs.sikkim_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.sikkim_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tamil_nadu_engg_jobs(request):
        try:
            job         = EnggJobs.tamil_nadu_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.tamil_nadu_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_telengana_engg_jobs(request):
        try:
            job         = EnggJobs.telangana_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.telangana_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_tripura_engg_jobs(request):
        try:
            job         = EnggJobs.tripura_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.tripura_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttarakhand_engg_jobs(request):
        try:
            job         = EnggJobs.uttarakhand_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.uttarakhand_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_uttar_pradesh_engg_jobs(request):
        try:
            job         = EnggJobs.uttar_pradesh_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.uttar_pradesh_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_west_bengal_engg_jobs(request):
        try:
            job         = EnggJobs.west_bengal_engg_jobs(request)
            sleep(0.5)
            job_details = EnggJobDetails.west_bengal_engg_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors
class RailwayJobs:
    def call_railway_jobs(request):
        try:
            job         = RailwayJob.railway_jobs(request)
            sleep(0.5)
            job_details = RailwayJobDetails.railway_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

class PoliceJobs:
    def call_police_defence_jobs(request):
        try:
            job         = PoliceDefenceJobs.police_defence_jobs(request)
            sleep(0.5)
            job_details = PoliceDefenceJobDetails.police_defence_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors

    def call_statewise_police_jobs(request):
        try:
            job         = PoliceDefenceJobs.statewise_police_jobs(request)
            sleep(0.5)
            job_details = PoliceDefenceJobDetails.statewise_police_job_details(request)
            message = call_all(job,job_details)
            return HttpResponse(message)
        except Exception  as e :
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errors = HandleError.make_error(traceback.format_exc(),e,fname,exc_type,exc_obj,exc_tb.tb_lineno)
            return errors
