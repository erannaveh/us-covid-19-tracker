use covid;
update us_totals s1, (select min(data_date) md from us_totals) s2 set cases_diff = cases, deaths_diff = deaths where data_date = s2.md;
update us_totals s1, us_totals s2 set s1.cases_diff = s1.cases-s2.cases, s1.deaths_diff = s1.deaths - s2.deaths where s1.data_date = (s2.data_date + INTERVAL 1 DAY);
update us_totals set cases_diff = 0 where cases_diff < 0;
update us_totals set deaths_diff = 0 where deaths_diff < 0;
update us_totals set death_rate = deaths/cases where cases>0;
update us_totals set cases_per_1m=((cases/population)*1000000), deaths_per_1m=((deaths/population)*1000000);

