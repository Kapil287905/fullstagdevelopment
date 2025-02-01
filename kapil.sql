create database hospital2025;
use hospital2025;

-- Doctors Table
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    office_location VARCHAR(255)
);

-- Patients Table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(10),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- Appointments Table
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_id INT,
    patient_id INT,
    appointment_date DATETIME NOT NULL,
    reason TEXT,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);


INSERT INTO Doctors (first_name, last_name, specialty, phone_number, email, office_location)
VALUES
('John', 'Doe', 'Cardiologist', '555-1234', 'john.doe@hospital.com', '123 Heart St, Cityville'),
('Jane', 'Smith', 'Neurologist', '555-2345', 'jane.smith@clinic.com', '456 Brain Ave, Townsville'),
('Alan', 'Johnson', 'Orthopedic', '555-3456', 'alan.johnson@health.com', '789 Bone Blvd, Villageburg'),
('Emily', 'Davis', 'Pediatrician', '555-4567', 'emily.davis@kidsclinic.com', '101 Kids Pkwy, Littletown'),
('Michael', 'Brown', 'Dermatologist', '555-5678', 'michael.brown@skincare.com', '202 Skin Dr, Suburbia'),
('Sophia', 'Wilson', 'Endocrinologist', '555-6789', 'sophia.wilson@hormones.com', '303 Endo Lane, Metropolis'),
('David', 'Lee', 'Oncologist', '555-7890', 'david.lee@cancercenter.com', '404 Care Blvd, Bigcity'),
('Olivia', 'Garcia', 'Gastroenterologist', '555-8901', 'olivia.garcia@digestive.com', '505 Gastro Rd, Smallville'),
('Lucas', 'Martinez', 'Psychiatrist', '555-9012', 'lucas.martinez@mentalhealth.com', '606 Mind St, Newtown'),
('Isabella', 'Rodriguez', 'Ophthalmologist', '555-0123', 'isabella.rodriguez@eyes.com', '707 Vision Ave, Riverside');


INSERT INTO Patients (first_name, last_name, date_of_birth, gender, phone_number, email, address)
VALUES
('Michael', 'Anderson', '1990-04-12', 'Male', '555-1111', 'michael.anderson@email.com', '123 Elm St, Cityville'),
('Sarah', 'Thomas', '1985-08-22', 'Female', '555-2222', 'sarah.thomas@email.com', '456 Oak St, Townsville'),
('James', 'Miller', '2000-11-10', 'Male', '555-3333', 'james.miller@email.com', '789 Pine St, Villageburg'),
('Emma', 'Wilson', '1995-02-19', 'Female', '555-4444', 'emma.wilson@email.com', '101 Maple St, Littletown'),
('Olivia', 'Moore', '1988-07-25', 'Female', '555-5555', 'olivia.moore@email.com', '202 Cedar St, Suburbia'),
('Liam', 'Taylor', '1979-09-03', 'Male', '555-6666', 'liam.taylor@email.com', '303 Birch Rd, Metropolis'),
('Sophia', 'Martin', '1992-12-14', 'Female', '555-7777', 'sophia.martin@email.com', '404 Willow Ave, Bigcity'),
('William', 'Lee', '1993-03-11', 'Male', '555-8888', 'william.lee@email.com', '505 Elm St, Smallville'),
('Ava', 'Young', '2001-05-18', 'Female', '555-9999', 'ava.young@email.com', '606 Pine Rd, Newtown'),
('Ethan', 'Harris', '1987-01-30', 'Male', '555-0000', 'ethan.harris@email.com', '707 Oak Blvd, Riverside');


INSERT INTO Appointments (doctor_id, patient_id, appointment_date, reason, status)
VALUES
(1, 1, '2025-01-10 09:00:00', 'Routine checkup', 'Completed'),
(2, 2, '2025-01-12 10:30:00', 'Neurological exam', 'Completed'),
(3, 3, '2025-01-15 14:00:00', 'Knee pain consultation', 'Pending'),
(4, 4, '2025-01-17 16:00:00', 'Annual pediatric checkup', 'Completed'),
(5, 5, '2025-01-19 11:30:00', 'Skin rash diagnosis', 'Canceled'),
(6, 6, '2025-01-20 08:30:00', 'Hormonal imbalance treatment', 'Pending'),
(7, 7, '2025-01-22 13:00:00', 'Cancer screening consultation', 'Completed'),
(8, 8, '2025-01-23 15:00:00', 'Digestive issues', 'Completed'),
(9, 9, '2025-01-24 11:00:00', 'Mental health evaluation', 'Completed'),
(10, 10, '2025-01-26 09:30:00', 'Eye exam and vision correction', 'Pending');

select * from Doctors;
desc Doctors;
select * from Patients;
desc Patients;
select * from Appointments;
desc Appointments;

-- Q.1 Find all doctors and their appointments, even if some doctors don't have any appointments yet.
select d.first_name,d.last_name,count(a.appointment_id) from Doctors d,Appointments a where d.doctor_id=a.doctor_id group by d.doctor_id;

-- Q.2 Find the number of appointments for each patient
select p.first_name,p.last_name,count(a.appointment_id) from Patients p,Appointments a where p.patient_id=a.patient_id group by p.patient_id;

-- Q.3 Find doctors who have appointments with all patients
-- Q.4 Find the doctor with the most appointments
select d.first_name,d.last_name from Doctors d join Appointments a where d.doctor_id=a.doctor_id;

-- Q.5 Find doctors who have at least one patient with an appointment after January 20, 2025
select distinct d.first_name,d.last_name,a.appointment_date from Doctors d join Appointments a on d.doctor_id=a.doctor_id where a.appointment_date > '2025-01-20 08:30:00';

-- Q.6 Get the count of appointments per doctor, with a subquery to select only doctors who have appointments after January 20, 2025
select d.first_name,d.last_name,a.appointment_date from Doctors d join Appointments a on d.doctor_id=a.doctor_id where a.appointment_date > '2025-01-20 08:30:00';

-- Q.7 Find how many appointments each doctor has.
select d.first_name,d.last_name,a.appointment_id from Doctors d,Appointments a where d.doctor_id/a.doctor_id  group by d.doctor_id;
-- Q.8 Find doctors who have more than 2 appointments.
select d.first_name,d.last_name,count(a.appointment_id) from Doctors d,Appointments a where d.doctor_id=a.doctor_id > 2;
-- Q.9 Find the average number of appointments each doctor has, but only for doctors with more than 1 appointment.
select d.first_name,d.last_name,avg(a.appointment_id)/avg(a.doctor_id) from Doctors d,Appointments a where d.doctor_id=a.doctor_id group by d.doctor_id having avg(a.appointment_id)/avg(a.doctor_id)>1;

-- Q.10 This query uses a self join to find doctors who have appointments with the same patients:
-- Q.11 Get the full details of doctors, patients, and the appointments they have:
select * from Doctors d,Patients p where (select a.appointment_id from Appointments a where d.doctor_id=a.doctor_id and p.patient_id=a.patient_id);

-- Q.12 Find the most recent appointment for each patient
select p.first_name,p.last_name,a.appointment_date from Patients p join Appointments a on p.patient_id=a.patient_id where a.appointment_date > '2025-01-20 08:30:00';

-- Q.13 Find doctors with no appointments
select d.first_name,d.last_name,a.appointment_id from Doctors d,Appointments a where a.appointment_id is null;

-- Q.14 Count appointments for each doctor after a certain date
select d.first_name,d.last_name,a.appointment_date from Doctors d join Appointments a on d.doctor_id=a.doctor_id where a.appointment_date > '2025-01-15 08:30:00';

-- Q.15 Find the average number of appointments per doctor
select d.first_name,d.last_name,avg(a.appointment_id)/avg(a.doctor_id) from Doctors d,Appointments a where d.doctor_id=a.doctor_id group by d.doctor_id;
