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


insert into firesale_seller(seller_id) values (1);
insert into firesale_seller(seller_id) values (2);
insert into firesale_seller(seller_id) values (3);
insert into firesale_buyer(buyer_id) values (1);
insert into firesale_buyer(buyer_id) values (2);
insert into firesale_buyer(buyer_id) values (3);

insert into firesale_item(name, highest_offer, condition, description, available, seller_id)
values ('Note book', 0, 'Good', 'Some book that is really good and useful', true, 3),
       ('Threads', 0, 'Normal', 'Some old threads', true, 2),
       ('Old T-shirt', 0, 'Good', 'A cute cat t-shirt', true, 3),
       ('Old camera', 0, 'Good', 'Useful camera', true, 2),
       ('Unused Duracell batteries', 0, 'Good as new', 'Some batteries I have laying around, unused', true, 3),
       ('Vintage book', 0, 'Good', 'This book is unused', true, 3),
       ('Comic book', 0, 'Slightly good', 'Some comic book I have laying around', true, 3),
       ('Handmade bear plush', 0, 'Good as new', 'Handmade knitted plushie bear children toy', true, 2),
       ('Handmade cat plush', 0, 'Good as new', 'Handmade knitted plushie cat children toy', true, 2),
       ('Handmade bunny plush', 0, 'Good as new', 'Handmade knitted plushie bunny children toy', true, 2);

insert into firesale_itemimage(image, item_id)
Values('images/notebook.png',1),
      ('images/threads.png',2),
      ('images/cat_tshirt.png',3),
      ('images/old_camera.png',4),
      ('images/batteries.png',5),
      ('images/vintagebook1.jpg',6),
      ('images/vintagebook2.jpg',6),
      ('images/comicbook.jpg',7),
      ('images/bearplush.png',8),
      ('images/catplush.png',9),
      ('images/bunnyplush.png',10);


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

