app_name = "globish_event_calendar"
app_title = "Globish Event Calendar"
app_publisher = "Internal Use"
app_description = "Globish Event Calendar"
app_email = "pichitchai@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "globish_event_calendar",
# 		"logo": "/assets/globish_event_calendar/logo.png",
# 		"title": "Globish Event Calendar",
# 		"route": "/globish_event_calendar",
# 		"has_permission": "globish_event_calendar.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/globish_event_calendar/css/globish_event_calendar.css"
# app_include_js = "/globish_event_calendar/event_calendar.js"
# app_include_js = "/assets/globish_event_calendar/js/calendar_overrides3.js"

# include js, css files in header of web template
# web_include_css = "/assets/globish_event_calendar/css/globish_event_calendar.css"
# web_include_js = "/assets/globish_event_calendar/js/globish_event_calendar.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "globish_event_calendar/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_calendar_js = {"Event" : "public/js/custom_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "globish_event_calendar/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "globish_event_calendar.utils.jinja_methods",
# 	"filters": "globish_event_calendar.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "globish_event_calendar.install.before_install"
# after_install = "globish_event_calendar.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "globish_event_calendar.uninstall.before_uninstall"
# after_uninstall = "globish_event_calendar.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "globish_event_calendar.utils.before_app_install"
# after_app_install = "globish_event_calendar.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "globish_event_calendar.utils.before_app_uninstall"
# after_app_uninstall = "globish_event_calendar.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "globish_event_calendar.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"globish_event_calendar.tasks.all"
# 	],
# 	"daily": [
# 		"globish_event_calendar.tasks.daily"
# 	],
# 	"hourly": [
# 		"globish_event_calendar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"globish_event_calendar.tasks.weekly"
# 	],
# 	"monthly": [
# 		"globish_event_calendar.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "globish_event_calendar.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"frappe.desk.doctype.event.event.get_events": "globish_event_calendar.controllers.override.custom_get_events",
    "frappe.desk.calendar.get_events": "globish_event_calendar.controllers.override.get_calendar_view_events"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "globish_event_calendar.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["globish_event_calendar.utils.before_request"]
# after_request = ["globish_event_calendar.utils.after_request"]

# Job Events
# ----------
# before_job = ["globish_event_calendar.utils.before_job"]
# after_job = ["globish_event_calendar.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"globish_event_calendar.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    "Custom Field"
]