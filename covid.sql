alter view vi_us_states as select state, max(cases) as cases, max(deaths) as deaths, max(data_date) as data_date from states group by state;

alter view vi_us_states as select state, cases, deaths, data_date from states where data_date = (select max(data_date) from states);

alter view vi_states as select s1.state, s1.cases, s1.deaths, s2.population, s1.data_date from vi_us_states s1, us_states s2 where s1.state = s2.state;
select * from vi_states;

select count(distinct(state)) from states;
select count(*) from us_states; 
create view vi_states as select s1.*, s1.cases-s2.cases as case_diff, s1.deaths - s2.deaths as death_diff from vi_states_base s1, states s2 where s1.state=s2.state and s2.data_date = date_sub(s1.data_date, interval 1 day);



create view vi_counties as select c1.*, c1.cases-c3.cases as case_diff, c1.deaths-c3.deaths as death_diff 
	from  counties c1, 
    (select state, county, max(data_date) as data_date from counties group by state, county) c2, 
    counties c3     
    where     c1.state = c2.state and c1.county = c2.county and c1.data_date = c2.data_date and 
              c1.state = c3.state and c1.county = c3.county and c3.data_date = date_sub(c1.data_date, interval 1 day);
    
    counties c2 where c1.county=c2.county and c2.data_date = date_sub(c1.data_date, interval 1 day);

select * from vi_counties;
select * from vi_states;