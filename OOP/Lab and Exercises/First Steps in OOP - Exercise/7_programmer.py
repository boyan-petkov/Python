# Create a class called Programmer. Upon initialization it should receive name (string), language (string), skills (integer). 
# The class should have two methods:
# -	watch_course(course_name, language, skills_earned)
# o	If the programmer's language is the same as the one on the course, 
# increase his skills with the given amount and return a message "{name} watched {course_name}".
# o	Otherwise return "{name} does not know {language}".
# -	change_language(new_language, skills_needed) 
# o	If the programmer has the skills and the new language is not the same as his, 
# change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
# o	If the programmer has the skills, but the given language is equal to his return "{name} already knows {language}".
# o	In the last case the programmer does not have the skills, so return "{name} needs {needed_skills} more skills" and do not change his language
# Submit only the class in the judge system.

