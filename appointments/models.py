# from django.db import models
# from doctors.models import Doctor
# from patients.models import Patient


# class Appointment(models.Model):

#     doctor = models.ForeignKey(
#         Doctor,
#         on_delete=models.CASCADE
#     )

#     patient = models.ForeignKey(
#         Patient,
#         on_delete=models.CASCADE
#     )

#     appointment_date = models.DateField()

#     def __str__(self):

#         return f"{self.patient} - {self.doctor}"



from django.db import models
from doctors.models import Doctor
from patients.models import Patient


class Appointment(models.Model):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    def __str__(self):

        return f"{self.patient.name} - {self.doctor.name}"