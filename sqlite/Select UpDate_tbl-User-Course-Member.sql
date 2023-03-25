SELECT Member.user_id, Member.course_id,User.name,Member.role 
FROM User JOIN Course JOIN Member
 ON Member.user_id = User.id AND Member.course_id=Course.id
WHERE  Member.role=0 AND User.name = "Ed" AND Course.title="Python"