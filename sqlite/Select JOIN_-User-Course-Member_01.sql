UPDATE Member
SET role = 1 
FROM (
    SELECT Member.course_id,Member.user_id,User.name,Member.role 
    FROM User JOIN Course JOIN Member
    ON Member.user_id = User.id AND Member.course_id=Course.id
    WHERE  Member.role=0 AND User.name = "Ed" AND Course.title="Python") AS rs
WHERE rs.user_id=Member.user_id AND  rs.course_id=Member.course_id
