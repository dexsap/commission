SELECT joborder.report_no, employee.employee_id, employee_fname, joborder_no, process
FROM employee, joborder,productivity
WHERE employee.employee_id = productivity.employee_id
AND joborder.report_no = productivity.report_no;