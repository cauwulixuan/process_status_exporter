# process_status_exporter
A prometheus exporter to scrape process status including CPU, Memory, Create time, process state and so on.

Usage:
python process_status_exporter.py process_info.txt
You can simply change the process_info.txt file to add or remove the process name you want to monitor.

after register in Prometheus server, results in url (http://hostname:9108/metrics) are as blow:
```
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 456679424.0
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 19083264.0
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1529719039.66
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 292.62
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 8.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="5",version="2.7.5"} 1.0
# HELP ambari_server_process_up ambari_server Process Up or Down (1 for up, 0 for down).
# TYPE ambari_server_process_up gauge
ambari_server_process_up 0.0
# HELP ambari_agent_process_up ambari_agent Process Up or Down (1 for up, 0 for down).
# TYPE ambari_agent_process_up gauge
ambari_agent_process_up 1.0
# HELP ambari_agent_running_time_seconds_total ambari_agent Total Running time in seconds.
# TYPE ambari_agent_running_time_seconds_total gauge
ambari_agent_running_time_seconds_total 1529720115.63
# HELP ambari_agent_cpu_percentage ambari_agent CPU Percentage.
# TYPE ambari_agent_cpu_percentage gauge
ambari_agent_cpu_percentage 0.0
# HELP ambari_agent_opened_fds_number ambari_agent Total Number of Opened fds.
# TYPE ambari_agent_opened_fds_number gauge
ambari_agent_opened_fds_number 10.0
# HELP ambari_agent_threads_number ambari_agent Total Number of Threads.
# TYPE ambari_agent_threads_number gauge
ambari_agent_threads_number 9.0
# HELP ambari_agent_opened_files_number ambari_agent Total Number of opened files.
# TYPE ambari_agent_opened_files_number gauge
ambari_agent_opened_files_number 3.0
# HELP ambari_agent_io_counters ambari_agent IO counters.
# TYPE ambari_agent_io_counters gauge
ambari_agent_io_counters{type="read_count"} 36102920.0
ambari_agent_io_counters{type="write_count"} 5152037.0
ambari_agent_io_counters{type="read_bytes"} 778581504.0
ambari_agent_io_counters{type="write_bytes"} 17475211264.0
ambari_agent_io_counters{type="read_chars"} 93439079513.0
ambari_agent_io_counters{type="write_chars"} 16640194818.0
# HELP ambari_agent_cpu_time_seconds_total ambari_agent Total CPU time in seconds.
# TYPE ambari_agent_cpu_time_seconds_total gauge
ambari_agent_cpu_time_seconds_total{mode="user"} 2370.46
ambari_agent_cpu_time_seconds_total{mode="system"} 456.03
ambari_agent_cpu_time_seconds_total{mode="children_user"} 4721.46
ambari_agent_cpu_time_seconds_total{mode="children_system"} 1242.23
# HELP ambari_agent_memory_usage_bytes_total ambari_agent Memory Usage by each mode.
# TYPE ambari_agent_memory_usage_bytes_total gauge
ambari_agent_memory_usage_bytes_total{mode="rss"} 231018496.0
ambari_agent_memory_usage_bytes_total{mode="vms"} 2375016448.0
ambari_agent_memory_usage_bytes_total{mode="shared"} 5156864.0
ambari_agent_memory_usage_bytes_total{mode="text"} 4096.0
ambari_agent_memory_usage_bytes_total{mode="lib"} 0.0
ambari_agent_memory_usage_bytes_total{mode="data"} 2137083904.0
ambari_agent_memory_usage_bytes_total{mode="dirty"} 0.0
ambari_agent_memory_usage_bytes_total{mode="uss"} 225947648.0
ambari_agent_memory_usage_bytes_total{mode="pss"} 226667520.0
ambari_agent_memory_usage_bytes_total{mode="swap"} 0.0
# HELP keycloak_process_up keycloak Process Up or Down (1 for up, 0 for down).
# TYPE keycloak_process_up gauge
keycloak_process_up 1.0
# HELP keycloak_running_time_seconds_total keycloak Total Running time in seconds.
# TYPE keycloak_running_time_seconds_total gauge
keycloak_running_time_seconds_total 1529719352.42
# HELP keycloak_cpu_percentage keycloak CPU Percentage.
# TYPE keycloak_cpu_percentage gauge
keycloak_cpu_percentage 0.0
# HELP keycloak_opened_fds_number keycloak Total Number of Opened fds.
# TYPE keycloak_opened_fds_number gauge
keycloak_opened_fds_number 4.0
# HELP keycloak_threads_number keycloak Total Number of Threads.
# TYPE keycloak_threads_number gauge
keycloak_threads_number 1.0
# HELP keycloak_opened_files_number keycloak Total Number of opened files.
# TYPE keycloak_opened_files_number gauge
keycloak_opened_files_number 1.0
# HELP keycloak_io_counters keycloak IO counters.
# TYPE keycloak_io_counters gauge
keycloak_io_counters{type="read_count"} 260.0
keycloak_io_counters{type="write_count"} 55.0
keycloak_io_counters{type="read_bytes"} 0.0
keycloak_io_counters{type="write_bytes"} 0.0
keycloak_io_counters{type="read_chars"} 143967.0
keycloak_io_counters{type="write_chars"} 2362.0
# HELP keycloak_cpu_time_seconds_total keycloak Total CPU time in seconds.
# TYPE keycloak_cpu_time_seconds_total gauge
keycloak_cpu_time_seconds_total{mode="user"} 0.0
keycloak_cpu_time_seconds_total{mode="system"} 0.0
keycloak_cpu_time_seconds_total{mode="children_user"} 0.0
keycloak_cpu_time_seconds_total{mode="children_system"} 0.02
# HELP keycloak_memory_usage_bytes_total keycloak Memory Usage by each mode.
# TYPE keycloak_memory_usage_bytes_total gauge
keycloak_memory_usage_bytes_total{mode="rss"} 1519616.0
keycloak_memory_usage_bytes_total{mode="vms"} 115838976.0
keycloak_memory_usage_bytes_total{mode="shared"} 1290240.0
keycloak_memory_usage_bytes_total{mode="text"} 905216.0
keycloak_memory_usage_bytes_total{mode="lib"} 0.0
keycloak_memory_usage_bytes_total{mode="data"} 352256.0
keycloak_memory_usage_bytes_total{mode="dirty"} 0.0
keycloak_memory_usage_bytes_total{mode="uss"} 245760.0
keycloak_memory_usage_bytes_total{mode="pss"} 321536.0
keycloak_memory_usage_bytes_total{mode="swap"} 0.0
# HELP tomcat_master_process_up tomcat_master Process Up or Down (1 for up, 0 for down).
# TYPE tomcat_master_process_up gauge
tomcat_master_process_up 1.0
# HELP tomcat_master_running_time_seconds_total tomcat_master Total Running time in seconds.
# TYPE tomcat_master_running_time_seconds_total gauge
tomcat_master_running_time_seconds_total 1529719939.7
# HELP tomcat_master_cpu_percentage tomcat_master CPU Percentage.
# TYPE tomcat_master_cpu_percentage gauge
tomcat_master_cpu_percentage 0.0
# HELP tomcat_master_opened_fds_number tomcat_master Total Number of Opened fds.
# TYPE tomcat_master_opened_fds_number gauge
tomcat_master_opened_fds_number 116.0
# HELP tomcat_master_threads_number tomcat_master Total Number of Threads.
# TYPE tomcat_master_threads_number gauge
tomcat_master_threads_number 53.0
# HELP tomcat_master_opened_files_number tomcat_master Total Number of opened files.
# TYPE tomcat_master_opened_files_number gauge
tomcat_master_opened_files_number 89.0
# HELP tomcat_master_io_counters tomcat_master IO counters.
# TYPE tomcat_master_io_counters gauge
tomcat_master_io_counters{type="read_count"} 1149203.0
tomcat_master_io_counters{type="write_count"} 29286.0
tomcat_master_io_counters{type="read_bytes"} 656994304.0
tomcat_master_io_counters{type="write_bytes"} 812343296.0
tomcat_master_io_counters{type="read_chars"} 1567058058.0
tomcat_master_io_counters{type="write_chars"} 5278096.0
# HELP tomcat_master_cpu_time_seconds_total tomcat_master Total CPU time in seconds.
# TYPE tomcat_master_cpu_time_seconds_total gauge
tomcat_master_cpu_time_seconds_total{mode="user"} 269.96
tomcat_master_cpu_time_seconds_total{mode="system"} 18.42
tomcat_master_cpu_time_seconds_total{mode="children_user"} 14.79
tomcat_master_cpu_time_seconds_total{mode="children_system"} 0.98
# HELP tomcat_master_memory_usage_bytes_total tomcat_master Memory Usage by each mode.
# TYPE tomcat_master_memory_usage_bytes_total gauge
tomcat_master_memory_usage_bytes_total{mode="rss"} 1626423296.0
tomcat_master_memory_usage_bytes_total{mode="vms"} 7095181312.0
tomcat_master_memory_usage_bytes_total{mode="shared"} 13864960.0
tomcat_master_memory_usage_bytes_total{mode="text"} 4096.0
tomcat_master_memory_usage_bytes_total{mode="lib"} 0.0
tomcat_master_memory_usage_bytes_total{mode="data"} 6913855488.0
tomcat_master_memory_usage_bytes_total{mode="dirty"} 0.0
tomcat_master_memory_usage_bytes_total{mode="uss"} 1615208448.0
tomcat_master_memory_usage_bytes_total{mode="pss"} 1615713280.0
tomcat_master_memory_usage_bytes_total{mode="swap"} 0.0
# HELP tomcat_tenant_process_up tomcat_tenant Process Up or Down (1 for up, 0 for down).
# TYPE tomcat_tenant_process_up gauge
tomcat_tenant_process_up 1.0
# HELP tomcat_tenant_running_time_seconds_total tomcat_tenant Total Running time in seconds.
# TYPE tomcat_tenant_running_time_seconds_total gauge
tomcat_tenant_running_time_seconds_total 1529719997.05
# HELP tomcat_tenant_cpu_percentage tomcat_tenant CPU Percentage.
# TYPE tomcat_tenant_cpu_percentage gauge
tomcat_tenant_cpu_percentage 0.0
# HELP tomcat_tenant_opened_fds_number tomcat_tenant Total Number of Opened fds.
# TYPE tomcat_tenant_opened_fds_number gauge
tomcat_tenant_opened_fds_number 111.0
# HELP tomcat_tenant_threads_number tomcat_tenant Total Number of Threads.
# TYPE tomcat_tenant_threads_number gauge
tomcat_tenant_threads_number 56.0
# HELP tomcat_tenant_opened_files_number tomcat_tenant Total Number of opened files.
# TYPE tomcat_tenant_opened_files_number gauge
tomcat_tenant_opened_files_number 89.0
# HELP tomcat_tenant_io_counters tomcat_tenant IO counters.
# TYPE tomcat_tenant_io_counters gauge
tomcat_tenant_io_counters{type="read_count"} 1245635.0
tomcat_tenant_io_counters{type="write_count"} 24528.0
tomcat_tenant_io_counters{type="read_bytes"} 519876608.0
tomcat_tenant_io_counters{type="write_bytes"} 798830592.0
tomcat_tenant_io_counters{type="read_chars"} 1467050242.0
tomcat_tenant_io_counters{type="write_chars"} 4135647.0
# HELP tomcat_tenant_cpu_time_seconds_total tomcat_tenant Total CPU time in seconds.
# TYPE tomcat_tenant_cpu_time_seconds_total gauge
tomcat_tenant_cpu_time_seconds_total{mode="user"} 278.27
tomcat_tenant_cpu_time_seconds_total{mode="system"} 18.57
tomcat_tenant_cpu_time_seconds_total{mode="children_user"} 2.63
tomcat_tenant_cpu_time_seconds_total{mode="children_system"} 0.47
# HELP tomcat_tenant_memory_usage_bytes_total tomcat_tenant Memory Usage by each mode.
# TYPE tomcat_tenant_memory_usage_bytes_total gauge
tomcat_tenant_memory_usage_bytes_total{mode="rss"} 1587953664.0
tomcat_tenant_memory_usage_bytes_total{mode="vms"} 7079358464.0
tomcat_tenant_memory_usage_bytes_total{mode="shared"} 13856768.0
tomcat_tenant_memory_usage_bytes_total{mode="text"} 4096.0
tomcat_tenant_memory_usage_bytes_total{mode="lib"} 0.0
tomcat_tenant_memory_usage_bytes_total{mode="data"} 6898032640.0
tomcat_tenant_memory_usage_bytes_total{mode="dirty"} 0.0
tomcat_tenant_memory_usage_bytes_total{mode="uss"} 1576755200.0
tomcat_tenant_memory_usage_bytes_total{mode="pss"} 1577257984.0
tomcat_tenant_memory_usage_bytes_total{mode="swap"} 0.0
# HELP nginx_process_up nginx Process Up or Down (1 for up, 0 for down).
# TYPE nginx_process_up gauge
nginx_process_up 0.0
# HELP consul_process_up consul Process Up or Down (1 for up, 0 for down).
# TYPE consul_process_up gauge
consul_process_up 1.0
# HELP consul_running_time_seconds_total consul Total Running time in seconds.
# TYPE consul_running_time_seconds_total gauge
consul_running_time_seconds_total 1529718984.64
# HELP consul_cpu_percentage consul CPU Percentage.
# TYPE consul_cpu_percentage gauge
consul_cpu_percentage 0.0
# HELP consul_opened_fds_number consul Total Number of Opened fds.
# TYPE consul_opened_fds_number gauge
consul_opened_fds_number 70.0
# HELP consul_threads_number consul Total Number of Threads.
# TYPE consul_threads_number gauge
consul_threads_number 26.0
# HELP consul_opened_files_number consul Total Number of opened files.
# TYPE consul_opened_files_number gauge
consul_opened_files_number 3.0
# HELP consul_io_counters consul IO counters.
# TYPE consul_io_counters gauge
consul_io_counters{type="read_count"} 1780982.0
consul_io_counters{type="write_count"} 996245.0
consul_io_counters{type="read_bytes"} 28295168.0
consul_io_counters{type="write_bytes"} 90222592.0
consul_io_counters{type="read_chars"} 373287418.0
consul_io_counters{type="write_chars"} 282688153.0
# HELP consul_cpu_time_seconds_total consul Total CPU time in seconds.
# TYPE consul_cpu_time_seconds_total gauge
consul_cpu_time_seconds_total{mode="user"} 260.64
consul_cpu_time_seconds_total{mode="system"} 99.29
consul_cpu_time_seconds_total{mode="children_user"} 0.0
consul_cpu_time_seconds_total{mode="children_system"} 0.0
# HELP consul_memory_usage_bytes_total consul Memory Usage by each mode.
# TYPE consul_memory_usage_bytes_total gauge
consul_memory_usage_bytes_total{mode="rss"} 25735168.0
consul_memory_usage_bytes_total{mode="vms"} 57065472.0
consul_memory_usage_bytes_total{mode="shared"} 4489216.0
consul_memory_usage_bytes_total{mode="text"} 12333056.0
consul_memory_usage_bytes_total{mode="lib"} 0.0
consul_memory_usage_bytes_total{mode="data"} 24932352.0
consul_memory_usage_bytes_total{mode="dirty"} 0.0
consul_memory_usage_bytes_total{mode="uss"} 28471296.0
consul_memory_usage_bytes_total{mode="pss"} 28471296.0
consul_memory_usage_bytes_total{mode="swap"} 4096.0
# HELP mysqld_process_up mysqld Process Up or Down (1 for up, 0 for down).
# TYPE mysqld_process_up gauge
mysqld_process_up 1.0
# HELP mysqld_running_time_seconds_total mysqld Total Running time in seconds.
# TYPE mysqld_running_time_seconds_total gauge
mysqld_running_time_seconds_total 1529719147.55
# HELP mysqld_cpu_percentage mysqld CPU Percentage.
# TYPE mysqld_cpu_percentage gauge
mysqld_cpu_percentage 0.0
# HELP mysqld_opened_fds_number mysqld Total Number of Opened fds.
# TYPE mysqld_opened_fds_number gauge
mysqld_opened_fds_number 37.0
# HELP mysqld_threads_number mysqld Total Number of Threads.
# TYPE mysqld_threads_number gauge
mysqld_threads_number 24.0
# HELP mysqld_opened_files_number mysqld Total Number of opened files.
# TYPE mysqld_opened_files_number gauge
mysqld_opened_files_number 28.0
# HELP mysqld_io_counters mysqld IO counters.
# TYPE mysqld_io_counters gauge
mysqld_io_counters{type="read_count"} 785.0
mysqld_io_counters{type="write_count"} 378422.0
mysqld_io_counters{type="read_bytes"} 0.0
mysqld_io_counters{type="write_bytes"} 136118272.0
mysqld_io_counters{type="read_chars"} 5100607.0
mysqld_io_counters{type="write_chars"} 85810139.0
# HELP mysqld_cpu_time_seconds_total mysqld Total CPU time in seconds.
# TYPE mysqld_cpu_time_seconds_total gauge
mysqld_cpu_time_seconds_total{mode="user"} 15.96
mysqld_cpu_time_seconds_total{mode="system"} 8.51
mysqld_cpu_time_seconds_total{mode="children_user"} 0.0
mysqld_cpu_time_seconds_total{mode="children_system"} 0.0
# HELP mysqld_memory_usage_bytes_total mysqld Memory Usage by each mode.
# TYPE mysqld_memory_usage_bytes_total gauge
mysqld_memory_usage_bytes_total{mode="rss"} 173826048.0
mysqld_memory_usage_bytes_total{mode="vms"} 1272786944.0
mysqld_memory_usage_bytes_total{mode="shared"} 3690496.0
mysqld_memory_usage_bytes_total{mode="text"} 12115968.0
mysqld_memory_usage_bytes_total{mode="lib"} 0.0
mysqld_memory_usage_bytes_total{mode="data"} 1229209600.0
mysqld_memory_usage_bytes_total{mode="dirty"} 0.0
mysqld_memory_usage_bytes_total{mode="uss"} 172711936.0
mysqld_memory_usage_bytes_total{mode="pss"} 172825600.0
mysqld_memory_usage_bytes_total{mode="swap"} 7782400.0
# HELP slapd_process_up slapd Process Up or Down (1 for up, 0 for down).
# TYPE slapd_process_up gauge
slapd_process_up 1.0
# HELP slapd_running_time_seconds_total slapd Total Running time in seconds.
# TYPE slapd_running_time_seconds_total gauge
slapd_running_time_seconds_total 1529719171.49
# HELP slapd_cpu_percentage slapd CPU Percentage.
# TYPE slapd_cpu_percentage gauge
slapd_cpu_percentage 0.0
# HELP slapd_opened_fds_number slapd Total Number of Opened fds.
# TYPE slapd_opened_fds_number gauge
slapd_opened_fds_number 41.0
# HELP slapd_threads_number slapd Total Number of Threads.
# TYPE slapd_threads_number gauge
slapd_threads_number 7.0
# HELP slapd_opened_files_number slapd Total Number of opened files.
# TYPE slapd_opened_files_number gauge
slapd_opened_files_number 13.0
# HELP slapd_io_counters slapd IO counters.
# TYPE slapd_io_counters gauge
slapd_io_counters{type="read_count"} 947467.0
slapd_io_counters{type="write_count"} 594049.0
slapd_io_counters{type="read_bytes"} 2326528.0
slapd_io_counters{type="write_bytes"} 2564386816.0
slapd_io_counters{type="read_chars"} 93522505.0
slapd_io_counters{type="write_chars"} 140586184.0
# HELP slapd_cpu_time_seconds_total slapd Total CPU time in seconds.
# TYPE slapd_cpu_time_seconds_total gauge
slapd_cpu_time_seconds_total{mode="user"} 30.87
slapd_cpu_time_seconds_total{mode="system"} 15.43
slapd_cpu_time_seconds_total{mode="children_user"} 0.0
slapd_cpu_time_seconds_total{mode="children_system"} 0.0
# HELP slapd_memory_usage_bytes_total slapd Memory Usage by each mode.
# TYPE slapd_memory_usage_bytes_total gauge
slapd_memory_usage_bytes_total{mode="rss"} 44699648.0
slapd_memory_usage_bytes_total{mode="vms"} 608989184.0
slapd_memory_usage_bytes_total{mode="shared"} 2879488.0
slapd_memory_usage_bytes_total{mode="text"} 1826816.0
slapd_memory_usage_bytes_total{mode="lib"} 0.0
slapd_memory_usage_bytes_total{mode="data"} 541708288.0
slapd_memory_usage_bytes_total{mode="dirty"} 0.0
slapd_memory_usage_bytes_total{mode="uss"} 43753472.0
slapd_memory_usage_bytes_total{mode="pss"} 43923456.0
slapd_memory_usage_bytes_total{mode="swap"} 0.0
# HELP prometheus_process_up prometheus Process Up or Down (1 for up, 0 for down).
# TYPE prometheus_process_up gauge
prometheus_process_up 1.0
# HELP prometheus_running_time_seconds_total prometheus Total Running time in seconds.
# TYPE prometheus_running_time_seconds_total gauge
prometheus_running_time_seconds_total 1529719056.46
# HELP prometheus_cpu_percentage prometheus CPU Percentage.
# TYPE prometheus_cpu_percentage gauge
prometheus_cpu_percentage 0.0
# HELP prometheus_opened_fds_number prometheus Total Number of Opened fds.
# TYPE prometheus_opened_fds_number gauge
prometheus_opened_fds_number 71.0
# HELP prometheus_threads_number prometheus Total Number of Threads.
# TYPE prometheus_threads_number gauge
prometheus_threads_number 18.0
# HELP prometheus_opened_files_number prometheus Total Number of opened files.
# TYPE prometheus_opened_files_number gauge
prometheus_opened_files_number 18.0
# HELP prometheus_io_counters prometheus IO counters.
# TYPE prometheus_io_counters gauge
prometheus_io_counters{type="read_count"} 380946.0
prometheus_io_counters{type="write_count"} 164936.0
prometheus_io_counters{type="read_bytes"} 48599040.0
prometheus_io_counters{type="write_bytes"} 2635575296.0
prometheus_io_counters{type="read_chars"} 490520291.0
prometheus_io_counters{type="write_chars"} 2689819831.0
# HELP prometheus_cpu_time_seconds_total prometheus Total CPU time in seconds.
# TYPE prometheus_cpu_time_seconds_total gauge
prometheus_cpu_time_seconds_total{mode="user"} 330.07
prometheus_cpu_time_seconds_total{mode="system"} 50.05
prometheus_cpu_time_seconds_total{mode="children_user"} 0.0
prometheus_cpu_time_seconds_total{mode="children_system"} 0.0
# HELP prometheus_memory_usage_bytes_total prometheus Memory Usage by each mode.
# TYPE prometheus_memory_usage_bytes_total gauge
prometheus_memory_usage_bytes_total{mode="rss"} 179310592.0
prometheus_memory_usage_bytes_total{mode="vms"} 219574272.0
prometheus_memory_usage_bytes_total{mode="shared"} 6135808.0
prometheus_memory_usage_bytes_total{mode="text"} 19390464.0
prometheus_memory_usage_bytes_total{mode="lib"} 0.0
prometheus_memory_usage_bytes_total{mode="data"} 182497280.0
prometheus_memory_usage_bytes_total{mode="dirty"} 0.0
prometheus_memory_usage_bytes_total{mode="uss"} 185106432.0
prometheus_memory_usage_bytes_total{mode="pss"} 185106432.0
prometheus_memory_usage_bytes_total{mode="swap"} 0.0
# HELP grafana_server_process_up grafana_server Process Up or Down (1 for up, 0 for down).
# TYPE grafana_server_process_up gauge
grafana_server_process_up 1.0
# HELP grafana_server_running_time_seconds_total grafana_server Total Running time in seconds.
# TYPE grafana_server_running_time_seconds_total gauge
grafana_server_running_time_seconds_total 1529719088.98
# HELP grafana_server_cpu_percentage grafana_server CPU Percentage.
# TYPE grafana_server_cpu_percentage gauge
grafana_server_cpu_percentage 0.0
# HELP grafana_server_opened_fds_number grafana_server Total Number of Opened fds.
# TYPE grafana_server_opened_fds_number gauge
grafana_server_opened_fds_number 8.0
# HELP grafana_server_threads_number grafana_server Total Number of Threads.
# TYPE grafana_server_threads_number gauge
grafana_server_threads_number 18.0
# HELP grafana_server_opened_files_number grafana_server Total Number of opened files.
# TYPE grafana_server_opened_files_number gauge
grafana_server_opened_files_number 2.0
# HELP grafana_server_io_counters grafana_server IO counters.
# TYPE grafana_server_io_counters gauge
grafana_server_io_counters{type="read_count"} 44839.0
grafana_server_io_counters{type="write_count"} 4850.0
grafana_server_io_counters{type="read_bytes"} 24408064.0
grafana_server_io_counters{type="write_bytes"} 122880.0
grafana_server_io_counters{type="read_chars"} 14541638.0
grafana_server_io_counters{type="write_chars"} 9539007.0
# HELP grafana_server_cpu_time_seconds_total grafana_server Total CPU time in seconds.
# TYPE grafana_server_cpu_time_seconds_total gauge
grafana_server_cpu_time_seconds_total{mode="user"} 21.8
grafana_server_cpu_time_seconds_total{mode="system"} 4.71
grafana_server_cpu_time_seconds_total{mode="children_user"} 0.0
grafana_server_cpu_time_seconds_total{mode="children_system"} 0.0
# HELP grafana_server_memory_usage_bytes_total grafana_server Memory Usage by each mode.
# TYPE grafana_server_memory_usage_bytes_total gauge
grafana_server_memory_usage_bytes_total{mode="rss"} 28139520.0
grafana_server_memory_usage_bytes_total{mode="vms"} 1135288320.0
grafana_server_memory_usage_bytes_total{mode="shared"} 7200768.0
grafana_server_memory_usage_bytes_total{mode="text"} 23334912.0
grafana_server_memory_usage_bytes_total{mode="lib"} 0.0
grafana_server_memory_usage_bytes_total{mode="data"} 1103237120.0
grafana_server_memory_usage_bytes_total{mode="dirty"} 0.0
grafana_server_memory_usage_bytes_total{mode="uss"} 29175808.0
grafana_server_memory_usage_bytes_total{mode="pss"} 29182976.0
grafana_server_memory_usage_bytes_total{mode="swap"} 16384.0
```
