delete from django_migrations where app = 'firesale';

drop table firesale_user;
drop table firesale_item;
drop table firesale_itemimage;
drop table firesale_seller;
drop table firesale_buyer;
drop table firesale_offer;

select * from firesale_user;
select * from firesale_seller;
select * from firesale_item;
select * from firesale_itemimage;

insert into firesale_user(name) values ('YuYu');
insert into firesale_user(name) values ('FaFa');
insert into firesale_user(name) values ('MoMo');
insert into firesale_user(name) values ('SiSi');

insert into firesale_seller(seller_id) values (3);
insert into firesale_seller(seller_id) values (1);
insert into firesale_buyer(buyer_id) values (4);

insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Notebook', 0, 'Good', 'Some cute notebook that is really good and useful', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Threads', 0, 'Normal', 'Some old threads', true, 2);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('T-shirt', 0, 'Good', 'A cute cat t-shirt', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Old camera', 0, 'Good', 'Useful camera', true, 2);

insert into firesale_itemimage(image, item_id)
Values('notebook.png',1),
      ('threads.png',2),
      ('cat_tshirt.png',3),
      ('old_camera.png',4);