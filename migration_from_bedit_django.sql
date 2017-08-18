select * from brugis_inter.a40_school_zipcode;

select * from bedit_ecoles_postcode;

insert into bedit_ecoles_postcode
 select nextval('bedit_ecoles_postcode_id_seq') as id, 1 as create_uid, localtimestamp as create_date, postcode as name, 1 as write_uid, localtimestamp as write_date
 from brugis_inter.a40_school_zipcode;
 
delete  from bedit_ecoles_postcode where id < 6;

delete from bedit_ecoles_municipality;
select * from brugis_inter.a40_school_municipality;
insert into bedit_ecoles_municipality
  select nextval('bedit_ecoles_municipality_id_seq') as id, 1 as create_uid, localtimestamp as create_date, name as name, 1 as write_uid, localtimestamp as write_date
   from brugis_inter.a40_school_municipality;
   
select * from bedit_ecoles_school_type;   
select * from brugis_inter.a40_school_schooltype;
delete from bedit_ecoles_school_type;   
insert into bedit_ecoles_school_type
  select nextval('bedit_ecoles_school_type_id_seq') as id, 1 as create_uid, localtimestamp as create_date,  description as description, 1 as write_uid, localtimestamp as write_date, stype as name
   from brugis_inter.a40_school_schooltype;
   
select * from bedit_ecoles_company;   
select * from brugis_inter.a40_school_company;
delete from bedit_ecoles_activity;
delete from bedit_ecoles_company;
insert into bedit_ecoles_company
  select nextval('bedit_ecoles_company_id_seq') as id,
  		  1 as create_uid,
          name,
          (select bedit_ecoles_postcode.id from bedit_ecoles_postcode where name like brol.postcode_name), 
          brol.address,
          brol.polnum,
          1,
          localtimestamp,
          (select bedit_ecoles_municipality.id from bedit_ecoles_municipality where name like brol.municipality_name), 
          localtimestamp,
          brol.the_geom
         from (select brugis_inter.a40_school_company.*, brugis_inter.a40_school_zipcode.postcode as postcode_name, brugis_inter.a40_school_municipality.name as municipality_name
               	from brugis_inter.a40_school_company
               		join brugis_inter.a40_school_zipcode on brugis_inter.a40_school_company.postcode_id = brugis_inter.a40_school_zipcode.postcode
               		join brugis_inter.a40_school_municipality on brugis_inter.a40_school_company.municipality_id = brugis_inter.a40_school_municipality.id
               ) as brol
               
 select * from bedit_ecoles_school; 
 select * from brugis_inter.a40_school_school;
 delete from bedit_ecoles_school;
 
 insert into bedit_ecoles_school
 	select nextval('bedit_ecoles_school_id_seq'),
    	1 as create_uid,
        (select bedit_ecoles_school_type.id from bedit_ecoles_school_type where name like brol.stype_name),
        brol.address,
        brol.polnum,
        1,
		localtimestamp,
        (select bedit_ecoles_municipality.id from bedit_ecoles_municipality where name like brol.municipality_name),
        localtimestamp,
        (select bedit_ecoles_postcode.id from bedit_ecoles_postcode where name like brol.postcode_name),
        brol.name,
        brol.the_geom
     from ( select brugis_inter.a40_school_school.*, brugis_inter.a40_school_zipcode.postcode as postcode_name, brugis_inter.a40_school_municipality.name as municipality_name, brugis_inter.a40_school_schooltype.stype as stype_name  
            from brugis_inter.a40_school_school
           		join brugis_inter.a40_school_zipcode on brugis_inter.a40_school_school.postcode_id = brugis_inter.a40_school_zipcode.postcode
           		join brugis_inter.a40_school_municipality on brugis_inter.a40_school_school.municipality_id = brugis_inter.a40_school_municipality.id
        		join brugis_inter.a40_school_schooltype on brugis_inter.a40_school_school.stype_id = brugis_inter.a40_school_schooltype.id ) as brol

DELETE FROM bedit_ecoles_school
WHERE id IN (SELECT id
              FROM (SELECT id,
                             ROW_NUMBER() OVER (partition BY name, address, stype_id ORDER BY id) AS rnum
                     FROM bedit_ecoles_school) t
              WHERE t.rnum > 1);
              
select * from  bedit_ecoles_activity;    
select * from  brugis_inter.a40_school_activity;

insert into bedit_ecoles_activity
	select nextval('bedit_ecoles_activity_id_seq'),
    1,
    brol.description,
    brol.number,
    (select  bedit_ecoles_company.id from bedit_ecoles_company where bedit_ecoles_company.name like brol.company_name),
    localtimestamp,
    brol.year,
    localtimestamp,
    1,
    ( select bedit_ecoles_school.id
     	from bedit_ecoles_school
     		join bedit_ecoles_school_type on bedit_ecoles_school.stype_id = bedit_ecoles_school_type.id
     	where bedit_ecoles_school.name like brol.school_name
     	and bedit_ecoles_school.address like brol.school_address
     	and bedit_ecoles_school_type.name like brol.school_stype
    )
    from (select brugis_inter.a40_school_activity.*,
            brugis_inter.a40_school_company.name as company_name,
            brugis_inter.a40_school_school.name as school_name,
            brugis_inter.a40_school_school.address as school_address,
			brugis_inter.a40_school_schooltype.stype as school_stype
          from brugis_inter.a40_school_activity
          join brugis_inter.a40_school_company on brugis_inter.a40_school_activity.company_id = brugis_inter.a40_school_company.id
          join brugis_inter.a40_school_school on brugis_inter.a40_school_activity.school_id = brugis_inter.a40_school_school.id
          join brugis_inter.a40_school_schooltype on brugis_inter.a40_school_schooltype.id = brugis_inter.a40_school_school.stype_id
    ) as brol;
    
    select * from brugis_inter.a40_school_activity
    join brugis_inter.a40_school_school on brugis_inter.a40_school_activity.school_id = brugis_inter.a40_school_school.id
    where brugis_inter.a40_school_school.name in (
        select name from brugis_inter.a40_school_school group by name, address, stype_id having count(1) > 1
    )

    select * from brugis_inter.a40_school_school where name like 'CAMPUS SAINT-JEAN';

       select count(1) from brugis_inter.a40_school_activity   
          


