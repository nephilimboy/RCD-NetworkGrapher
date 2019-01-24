# class EmployeeEvent(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     event_name = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#
# class EmployeeEvent_Users(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     employee_event = models.ForeignKey(EmployeeEvent, on_delete=models.CASCADE,
#                                        related_name='employee_event_employee_list')
#
#     employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
#                                  related_name='employeeEvent_employee')
#
#
# class EmployeeEventUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeEvent_Users
#         fields = ('id', 'employee',)
#
#
# class EmployeeEventSerializer(serializers.ModelSerializer):
#     employee_event_users = EmployeeEventUserSerializer(required=True, many=True)
#
#     class Meta:
#         model = EmployeeEvent
#         fields = ('event_name', 'start_date', 'end_date', 'employee_event_users',)
#
#     def create(self, validated_data):
#         request = self.context.get('request')
#         employee_event = EmployeeEvent.objects.create(
#             event_name=validated_data['event_name'],
#             start_date=validated_data['start_date'],
#             end_date=validated_data['end_date'],
#             # etc ...
#         )
#         employeeEventUsers_data = validated_data.pop('employee_event_users', [])
#
#         for employeeEventUser_data in employeeEventUsers_data:
#             employeeEvent_users = EmployeeEvent_Users.objects.create(
#                 employee_event=employee_event,
#                 employee=employeeEventUser_data['employee'],
#
#             )
#         employee_event.employee_event_users = employeeEventUsers_data;
#         return employee_event
#
#     def update(self, instance, validated_data):
#
#         instance.event_name = validated_data['event_name']
#         instance.start_date = validated_data['start_date']
#         instance.end_date = validated_data['end_date']
#         instance.save()
#
#         instance.employee_event_users = validated_data.get('employee_event_users')
#
#         if instance.employee_event_users:
#             for employee_event_user in instance.employee_event_users:
#                 employee_event_user_id = employee_event_user.get('employee_id', None)
#                 if employee_event_user_id:
#                     emp_user = EmployeeEvent_Users.objects.get(id=employee_event_user_id, employee_event=instance)
#                     emp_user.employee = employee_event_user.get('employee', emp_user.employee)
#                     emp_user.save()
#                 else:
#                     EmployeeEvent_Users.objects.create(employee_event=instance, **employee_event_user)
#
#         return instance
#
#
#
#
#     def update(self, instance, validated_data):
#         instance.event_name = validated_data['event_name']
#         instance.start_date = validated_data['start_date']
#         instance.end_date = validated_data['end_date']
#
#         for employee_event_user in validated_data['employee_event_users']:
#             employee_event_user_id = employee_event_user.get('employee_id', None)
#             if employee_event_user_id:
#                 emp_user = EmployeeEvent_Users.objects.get(id=employee_event_user_id, employee_event=instance)
#                 emp_user.employee = employee_event_user.get('employee', emp_user.employee)
#                 emp_user.save()
#             else:
#                 user = EmployeeEvent_Users.objects.create(employee_event=instance, **employee_event_user)
#                 user.save()
#                 instance.employee_event_users.add(user)
#
#         instance.save()
#         return instance
x = 306
for d in range(1, 25):
    x = x + 306 + 5*d
print(x)