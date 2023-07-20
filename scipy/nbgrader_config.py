from ngshare_exchange import configureExchange

c = get_config()

# NOTE: ngshare wants the hub prefix (eg, 202x-QTR-COURSE) in the exchange path. This will get mounted dynamically by Kuberntes by a configMap
configureExchange(
    c, 'http://ngshare:8080/services/ngshare'
)

# Add the following to let students access courses without configuration
# For more information, read Notes for Instructors in the documentation
c.CourseDirectory.course_id = '*'
