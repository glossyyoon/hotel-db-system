from django.db import models

# Create your models here.


class Guest(models.Model):
    objects = models.Manager()
    is_guest = models.BooleanField(default=True)
    site_id = models.CharField(max_length=20)
    site_pw = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nation = models.CharField(max_length=40, null=True)
    gender = models.CharField(max_length=1, null=True)
    email = models.CharField(max_length=40, null=True)
    birthday = models.DateField(null=True)
    reseve_num = models.IntegerField(null=True)
    car_num = models.IntegerField(null=True)
    is_pad = models.BooleanField(default=True, null=True)
    card_cvc_num = models.IntegerField(null=True)
    card_experiment = models.IntegerField(null=True)
    card_password = models.IntegerField(null=True)
    room_person_cnt = models.IntegerField(null=True)
    room_type = models.CharField(max_length=20, null=True)
    check_in = models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)
    room_service_fee = models.IntegerField(null=True)
    guest_point = models.IntegerField(null=True)

    def __str__(self):
        return f'ID: {self.site_id} NAME: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'guest'


class Staff(models.Model):
    objects = models.Manager()
    staff_id = models.IntegerField(default=0)
    department_type = (('CLE', 'Cleaning'),
                       ('TSD', 'Technical Support Department'),
                       ('CRD', 'Customer Response Department'), ('MAN', 'Manager Department'))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nation = models.CharField(max_length=40)
    gender_type = (('MALE', 'Male'),
                   ('FEMALE', 'Female'),)
    gender = models.CharField(
        max_length=6, choices=gender_type, default="Male")
    birthday = models.DateField()
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=50)
    hire_date = models.DateField()
    salary = models.IntegerField()
    position = models.CharField(max_length=100)
    had_annual_leave = models.IntegerField(default=0)
    department = models.CharField(
        max_length=3, choices=department_type, default="None")

    def __str__(self):
        return f'ID: {self.staff_id} NAME: {self.first_name} {self.last_name} DEPARTMENT: {self.department}'

    class Meta:
        db_table = 'staff'


class Sales(models.Model):
    objects = models.Manager()
    date = models.DateTimeField()
    fee = models.IntegerField()
    payment_num = models.IntegerField()

    def __str__(self):
        return f'DATE: {self.date} FEE: {self.fee} payment_num: {self.payment_num}'

    class Meta:
        db_table = 'sales'


class Robot(models.Model):
    objects = models.Manager()
    work_check = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=False)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f'work_check: {self.work_check} is_emergency: {self.is_emergency} position: {self.position}'


class Attendance(models.Model):
    objects = models.Manager()
    staff_id = models.ForeignKey(
        'Staff', on_delete=models.CASCADE, db_column='staff_id')
    date = models.DateTimeField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    work_type = models.CharField(max_length=50)
    description = models.TextField()
    accecpt = models.BooleanField()


class StaffLeave(models.Model):
    staff_id = models.ForeignKey(
        'Staff', on_delete=models.CASCADE, db_column='staff_id')
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    leave_type = (('Monthly_Leave', 'Monthly_Leave'),
                  ('Annual_Leave', 'Annual_Leave'))
    accecpt = models.BooleanField()
