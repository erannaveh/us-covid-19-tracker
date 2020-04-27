use covid;

select "Updating counties" as message;

update counties s1, (select state, county, min(data_date) as data_date from counties group by state, county) s2 set s1.cases_diff = s1.cases, s1.deaths_diff = s1.deaths where s1.state = s2.state and s1.county = s2.county and s1.data_date = s2.data_date;
update counties s1, counties s2 set s1.cases_diff = s1.cases-s2.cases, s1.deaths_diff = s1.deaths - s2.deaths where s1.state = s2.state and s1.county = s2.county and s1.data_date = (s2.data_date + INTERVAL 1 DAY);
update counties set cases_diff = 0 where cases_diff < 0;
update counties set deaths_diff = 0 where deaths_diff < 0;
update counties s1, us_counties s2 set s1.cases_per_1k = ((s1.cases/s2.population)*1000), s1.deaths_per_1k=((s1.deaths/s2.population)*1000)  where s1.state=s2.state and s1.county=s2.county;

select "County information successfuly updated" as message;
