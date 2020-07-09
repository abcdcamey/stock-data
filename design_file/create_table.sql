CREATE TABLE stock_basic_list
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    symbol VARCHAR(56),
    name VARCHAR(56),
    area VARCHAR(56),
    industry VARCHAR(128),
    fullname VARCHAR(128),
    enname VARCHAR(128),
    market VARCHAR(128),
    exchange VARCHAR(128),
    curr_type VARCHAR(56),
    list_status VARCHAR(56),
    list_date VARCHAR(56),
    delist_date VARCHAR(56),
    is_hs VARCHAR(56),
    update_dt DATETIME
);



CREATE TABLE exchange_trade_cal
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    exchange VARCHAR(56),
    cal_date VARCHAR(56),
    is_open int,
    pretrade_date VARCHAR(56),
    update_dt DATETIME
);


CREATE TABLE hs_const_list
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    hs_type VARCHAR(56),
    in_date VARCHAR(56),
    out_date VARCHAR(56),
    is_new VARCHAR(56),
    update_dt DATETIME
);


CREATE TABLE stock_name_change
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    name VARCHAR(56),
    start_date VARCHAR(56),
    end_date VARCHAR(56),
    ann_date VARCHAR(56),
    change_reason VARCHAR(1024),
    update_dt DATETIME

);


CREATE TABLE stock_company_basic_info
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    exchange VARCHAR(56),
    chairman VARCHAR(56),
    manager VARCHAR(56),
    secretary VARCHAR(56),
    reg_capital FLOAT,
    setup_date VARCHAR(56),
    province VARCHAR(56),
    city VARCHAR(128),
    introduction VARCHAR(2048),
    website VARCHAR(2048),
    email VARCHAR(2048),
    office VARCHAR(2048),
    employees int,
    main_business VARCHAR(4096),
    business_scope VARCHAR(4096),
    update_dt DATETIME
);


CREATE TABLE new_share_list
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    sub_code VARCHAR(56),
    name VARCHAR(56),
    ipo_date VARCHAR(56),
    issue_date VARCHAR(56),
    amount FLOAT,
    market_amount FLOAT,
    price FLOAT,
    pe float,
    limit_amount FLOAT,
    funds FLOAT,
    ballot FLOAT,
    update_dt DATETIME
);


CREATE TABLE fact_market_stock_daily
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    trade_date VARCHAR(56),
    open float,
    high VARCHAR(56),
    low float,
    close float,
    pre_close float,
    `change` float,
    pct_chg float,
    vol float,
    amount float,
    update_dt DATETIME
);


CREATE TABLE fact_market_stock_weekly
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    trade_date VARCHAR(56),
    open float,
    high VARCHAR(56),
    low float,
    close float,
    pre_close float,
    `change` float,
    pct_chg float,
    vol float,
    amount float,
    update_dt DATETIME
);


CREATE TABLE fact_market_stock_monthly
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    trade_date VARCHAR(56),
    open float,
    high VARCHAR(56),
    low float,
    close float,
    pre_close float,
    `change` float,
    pct_chg float,
    vol float,
    amount float,
    update_dt DATETIME
);





CREATE TABLE fact_market_stock_suspend
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    suspend_date VARCHAR(56),
    resume_date VARCHAR(56),
    ann_date VARCHAR(56),
    suspend_reason VARCHAR(2048),
    reason_type VARCHAR(1024),
    update_dt DATETIME
);





CREATE TABLE fact_market_stock_daily_basic
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    trade_date VARCHAR(56),
    `close` DOUBLE,
    turnover_rate DOUBLE,
    turnover_rate_f DOUBLE,
    volume_ratio DOUBLE,
    pe DOUBLE,
    pe_ttm DOUBLE,
    pb DOUBLE,
    ps DOUBLE,
    ps_ttm DOUBLE,
    total_share DOUBLE,
    float_share DOUBLE,
    free_share DOUBLE,
    total_mv DOUBLE,
    circ_mv DOUBLE,
    update_dt DATETIME
);

CREATE TABLE fact_adj_factor
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    trade_date VARCHAR(56),
    adj_factor FLOAT,
    update_dt DATETIME
);




CREATE UNIQUE INDEX fact_market_stock_daily_basic_uk ON fact_market_stock_daily_basic (ts_code, trade_date);


CREATE UNIQUE INDEX fact_market_stock_monthly_uk ON fact_market_stock_monthly (ts_code, trade_date);


CREATE UNIQUE INDEX fact_market_stock_weekly_uk ON fact_market_stock_weekly (ts_code, trade_date);


CREATE UNIQUE INDEX fact_market_stock_daily_uk ON fact_market_stock_daily (ts_code, trade_date);


CREATE UNIQUE INDEX fact_adj_factor_uk ON fact_adj_factor (ts_code, trade_date);








#----------------市场参考数据# ----------------------------------

CREATE TABLE fact_moneyflow_hsgt
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    trade_date  VARCHAR(56),
	ggt_ss VARCHAR(128),
	ggt_sz VARCHAR(128),
	hgt VARCHAR(56),
	sgt VARCHAR(56),
	north_money VARCHAR(56),
	south_money VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_moneyflow_hsgt_uk ON fact_moneyflow_hsgt (trade_date);


CREATE TABLE fact_hsgt_top10
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    trade_date VARCHAR(56),
	ts_code VARCHAR(56),
	name VARCHAR(56),
	close double,
	`change` double,
	rank int,
	market_type VARCHAR(56),
	amount double,
	net_amount double,
	buy double,
	sell double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_hsgt_top10_uk ON fact_hsgt_top10 (trade_date,ts_code);









CREATE TABLE fact_ggt_top10
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	trade_date VARCHAR(56),
	ts_code VARCHAR(56),
	name VARCHAR(56),
	close double,
	p_change double,
	rank int,
	market_type VARCHAR(56),
	amount double,
	net_amount double,
	sh_amount double,
	sh_net_amount double,
	sh_buy double,
	sh_sell double,
	sz_amount double,
	sz_net_amount double,
	sz_buy double,
	sz_sell double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_ggt_top10_uk ON fact_ggt_top10 (trade_date,ts_code);




CREATE TABLE fact_margin
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	trade_date VARCHAR(56),
	exchange_id	VARCHAR(56),
	rzye double,
	rzmre double,
	rzche double,
	rqye double,
	rqmcl double,
	rzrqye double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_margin_uk ON fact_margin (trade_date,exchange_id);



CREATE TABLE fact_margin_detail
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    trade_date VARCHAR(56),
	ts_code	VARCHAR(56),
	rzye double,
	rqye double,
	rzmre double,
	rqyl double,
	rzche double,
	rqchl double,
	rqmcl double,
	rzrqye double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_margin_detail_uk ON fact_margin_detail (trade_date,ts_code);





CREATE TABLE fact_stock_top10_holders
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ts_code	VARCHAR(56),
	ann_date	VARCHAR(56),
	end_date	VARCHAR(56),
	holder_name	VARCHAR(56),
	hold_amount double,
	hold_ratio double,
    update_dt DATETIME
);

CREATE UNIQUE INDEX fact_stock_top10_holders_uk ON fact_stock_top10_holders (ts_code,ann_date,holder_name);




CREATE TABLE fact_stock_top10_floatholders
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ts_code	VARCHAR(56),
	ann_date	VARCHAR(56),
	end_date	VARCHAR(56),
	holder_name	VARCHAR(56),
	hold_amount double,
    update_dt DATETIME
);

CREATE UNIQUE INDEX fact_stock_top10_floatholders_uk ON fact_stock_top10_floatholders (ts_code,ann_date,holder_name);


CREATE TABLE fact_stock_daily_top_list
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    trade_date VARCHAR(56),
	ts_code VARCHAR(56),
	exalter	VARCHAR(56),
	buy	double,
	buy_rate double,
	sell double,
	sell_rate double,
	net_buy double,
    update_dt DATETIME
);

CREATE UNIQUE INDEX fact_stock_daily_top_list_uk ON fact_stock_daily_top_list (trade_date,ts_code);




CREATE TABLE fact_stock_daily_top_inst
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    trade_date VARCHAR(56),
	ts_code	VARCHAR(56),
	name VARCHAR(56),
	close double,
	pct_change double,
	turnover_rate double,
	amount double,
	l_sell double,
	l_buy double,
	l_amount double,
	net_amount double,
	net_rate double,
	amount_rate double,
	double_values double,
	reason VARCHAR(56),
    update_dt DATETIME
);

CREATE UNIQUE INDEX fact_stock_daily_top_inst_uk ON fact_stock_daily_top_inst (trade_date,ts_code);















CREATE TABLE fact_stock_pledge_stat
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	end_date VARCHAR(56),
	pledge_count int,
	unrest_pledge double,
	rest_pledge double,
	total_share double,
	pledge_ratio double,
    update_dt DATETIME
);




CREATE TABLE fact_stock_pledge_detail
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	ann_date VARCHAR(56),
	holder_name	VARCHAR(56),
	pledge_amount double,
	start_date VARCHAR(56),
	end_date VARCHAR(56),
	is_release VARCHAR(56),
	release_date VARCHAR(56),
	pledgor VARCHAR(56),
	holding_amount double,
	pledged_amount double,
	p_total_ratio double,
	h_total_ratio double,
	is_buyback VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_pledge_detail_uk ON fact_stock_pledge_detail (ts_code,ann_date);


CREATE TABLE fact_stock_repurchase
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	ann_date VARCHAR(56),
	end_date VARCHAR(56),
	proc VARCHAR(56),
	exp_date VARCHAR(56),
	vol double,
	amount double,
	high_limit double,
	low_limit double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_repurchase_uk ON fact_stock_repurchase (ts_code,ann_date);





CREATE TABLE fact_stock_concept
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    code VARCHAR(56),
	name VARCHAR(128),
	src VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_concept_uk ON fact_stock_concept (code);



CREATE TABLE fact_stock_concept_detail
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    concept_code VARCHAR(56),
	concept_name VARCHAR(128),
	ts_code VARCHAR(56),
	name VARCHAR(56),
	in_date VARCHAR(56),
	out_date VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_concept_detail_uk ON fact_stock_concept_detail (concept_code,ts_code);






CREATE TABLE fact_stock_share_double
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	ann_date VARCHAR(56),
	double_date VARCHAR(56),
	double_share double,
	double_ratio double,
	holder_name VARCHAR(56),
	share_type VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_share_double_uk ON fact_stock_share_double (ts_code,ann_date);



CREATE TABLE fact_stock_block_trade
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	trade_date VARCHAR(56),
	price double,
	vol double,
	amount double,
	buyer VARCHAR(56),
	seller VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_block_trade_uk ON fact_stock_block_trade (ts_code,trade_date);




CREATE TABLE fact_stock_stk_account
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    date VARCHAR(56),
	weekly_new double,
	total double,
	weekly_hold double,
	weekly_trade double,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_stk_account_uk ON fact_stock_stk_account (date);


CREATE TABLE fact_stock_stk_holdernumber
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
    ann_date VARCHAR(56),
    end_date VARCHAR(56),
    holder_num int,
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_stk_holdernumber_uk ON fact_stock_stk_holdernumber (ts_code,ann_date);



CREATE TABLE fact_stock_stk_holdertrade
(
    id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    ts_code VARCHAR(56),
	ann_date VARCHAR(56),
	holder_name VARCHAR(56),
	holder_type VARCHAR(56),
	in_de VARCHAR(56),
	change_vol double,
	change_ratio double,
	after_share double,
	after_ratio double,
	avg_price double,
	total_share double,
	begin_date VARCHAR(56),
	close_date VARCHAR(56),
    update_dt DATETIME
);
CREATE UNIQUE INDEX fact_stock_stk_holdertrade_uk ON fact_stock_stk_holdertrade (ts_code,ann_date,holder_name);





