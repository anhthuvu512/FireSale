delete from django_migrations where app = 'firesale';
delete from django_migrations where app = 'user';

drop table firesale_buyernotification;
drop table firesale_sellernotification;
drop table firesale_offer;
drop table firesale_buyer;
drop table firesale_itemimage;
drop table firesale_item cascade;
drop table firesale_seller cascade;

drop table user_profile;
drop table user_address;
drop table user_payment;
drop table user_rating;

select * from firesale_seller;
select * from firesale_item;
select * from firesale_itemimage;

insert into firesale_seller(seller_id) values (1);
insert into firesale_seller(seller_id) values (2);
insert into firesale_seller(seller_id) values (3);
insert into firesale_buyer(buyer_id) values (1);
insert into firesale_buyer(buyer_id) values (2);
insert into firesale_buyer(buyer_id) values (3);

insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Notebook', 0, 'Good', 'Some cute notebook that is really good and useful', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Threads', 0, 'Normal', 'Some old threads', true, 2);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('T-shirt', 0, 'Good', 'A cute cat t-shirt', true, 1);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Old camera', 0, 'Good', 'Useful camera', true, 2);
insert into firesale_item(name, highest_offer, condition, description, available, seller_id) values ('Unused batteries', 0, 'Good as new', 'Some batteries I have laying around, unused', true, 1);

insert into firesale_itemimage(image, item_id)
Values('images/notebook.png',1),
      ('images/threads.png',2),
      ('images/cat_tshirt.png',3),
      ('images/old_camera.png',4),
      ('images/batteries.png',5);

insert into firesale_offer(price, accepted, message, buyer_id, item_id, seller_id)
VALUES (500,false, 'me like', 3, 3, 1),
       (199,false, 'i need this badly', 3, 2, 2),
       (500,false, 'i like this one', 3, 4, 2),
       (99,false, 'i need this badly', 2, 5, 1),
       (599,false, 'i really like this', 1, 4, 2),
       (200,false, 'i need this badly', 1, 2, 2);

insert into firesale_sellernotification(notif, offer_id, receiver_id, sender_id)
VALUES ('otheruser offers 500kr for T-shirt', 1, 1 ,3),
       ('otheruser offers 199kr for Threads', 2, 2 ,3),
       ('otheruser offers 500kr for Old camera', 3, 2 ,3),
       ('newuser offers 99kr for Unused batteries', 4, 1 ,2),
       ('lorraine offers 599kr for Old camera', 5, 2 ,1),
       ('lorraine offers 200kr for Threads', 6, 2 ,1);

drop function if exists CheckOfferPrice();
create function CheckOfferPrice() returns trigger
as $$ begin
    if (new.price > (select highest_offer
                     from firesale_item
                     where id = new.item_id)) then
        update firesale_item
        set highest_offer = new.price
        where id = new.item_id;
    end if;
    return new;
end; $$ language  plpgsql;

drop trigger if exists CheckOfferPrice on "fire-sale-db";
create trigger CheckOfferPrice
after insert on firesale_offer
for each row execute procedure CheckOfferPrice();


drop function if exists AddNewUser();
create function AddNewUser() returns trigger
as $$ begin
    insert into firesale_seller(seller_id) values (new.id);
    insert into firesale_buyer(buyer_id) values (new.id);
    return new;
end; $$ language  plpgsql;

drop trigger if exists AddNewUser on "fire-sale-db";
create trigger AddNewUser
after insert on auth_user
for each row execute procedure AddNewUser();

