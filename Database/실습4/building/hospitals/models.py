from django.db import models

# Create your models here.
# 1:N 구현
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name} 전문의"
    
class Patient(models.Model):
    # 이러면 의사가 사라지면 환자도 사라진다.
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"

# M(의사):N(환자)
# 관계를 기억해주는 중계 테이블
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)    #FK
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  #FK

#     def __str__(self):
#         return f"{self.doctor_id}번 의사의 {self.patient_id}번 환자"