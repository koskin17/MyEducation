# Solve the problem of finding the tangent of the angle alpha given the sine of alpha and the cosine of alpha and add event logging to the "app.log" file.
# Catching the resulting sine and cosine values should be implemented using the "info" level.
# In the case of successful finding of the tangent of the alpha angle, logging should be with the "debug" level.
# In the event that cosine alpha = 0, logging should be with the "warning" level and the notification: "The cosine of the angle alpha = 0. The tangent is not defined.".
# In the event that the tangent is not defined, logging should be with the "critical" level and the notification: "The tangent of the angle alpha is not defined.".
# tan(α) = sin(α) / cos(α)
# Don't use: encoding='utf-8'.

# Don't use'print()'.

# Don't use'return'.

# Please use logging. ....



# For example:

# Тест	Input	Result
# print_file("app.log")
# sin_alpha = 0.5
# cos_alpha = math.sqrt(3) / 2

# sin_alpha = 0.5
# cos_alpha = 'w'

# sin_alpha = 0.5
# cos_alpha = 0
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = 0.8660254037844386
# DEBUG:root:The value of the tangent of the angle alpha is found = 0.5773502691896258
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = w
# CRITICAL:root:The tangent of the angle alpha is not defined.
# INFO:root:A value has been entered sin(alpha) = 0.5
# INFO:root:A value has been entered cos(alpha) = 0
# WARNING:root:The cosine of the angle alpha = 0. The tangent is not defined.