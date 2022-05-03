insert into firesale_user(name) values ('YuYu');
insert into firesale_user(name) values ('FaFa');
insert into firesale_user(name) values ('MoMo');
insert into firesale_user(name) values ('SiSi');

select * from firesale_user;

insert into firesale_seller(seller_id) values (3);
insert into firesale_seller(seller_id) values (1);
insert into firesale_buyer(buyer_id) values (4);

insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Notebook', 0, 'Good', 'Some cute notebook that is really good and useful', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Threads', 0, 'Normal', 'Some old threads', true, 2);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('T-shirt', 0, 'Good', 'A cute cat t-shirt', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Old camera', 0, 'Good', 'Useful camera', true, 2);