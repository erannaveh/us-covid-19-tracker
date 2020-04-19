use covid;
update states s1, (select state, min(data_date) as data_date from states group by state) s2 set s1.cases_diff = s1.cases, s1.deaths_diff = s1.deaths where s1.state = s2.state and s1.data_date = s2.data_date;
update states s1, states s2 set s1.cases_diff = s1.cases-s2.cases, s1.deaths_diff = s1.deaths - s2.deaths where s1.state = s2.state and s1.data_date = (s2.data_date + INTERVAL 1 DAY);
update states set cases_diff = 0 where cases_diff < 0;
update states set deaths_diff = 0 where deaths_diff < 0;
update states s1, us_states s2 set s1.cases_per_100k = ((s1.cases/s2.population)*100000), s1.deaths_per_100k=((s1.deaths/s2.population)*100000)  where s1.state=s2.state;

