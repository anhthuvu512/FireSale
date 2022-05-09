delete from django_migrations where app = 'firesale';
delete from django_migrations where app = 'user';

drop table firesale_buyernotification;
drop table firesale_sellernotification;
drop table firesale_offer;
drop table firesale_buyer;
drop table firesale_itemimage;
drop table firesale_item;
drop table firesale_seller cascade;

drop table user_profile;
drop table user_address;
drop table user_payment;

select * from firesale_seller;
select * from firesale_item;
select * from firesale_itemimage;
select * from user_profile;

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
Values('https://images.unsplash.com/photo-1625229086762-f06307638717?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80',1),
      ('https://images.unsplash.com/photo-1615486261304-6978e38f377a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',2),
      ('https://images.unsplash.com/photo-1576566588028-4147f3842f27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',3),
      ('https://images.unsplash.com/photo-1586527484765-979a20639316?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',4),
      ('https://images.unsplash.com/photo-1586527484765-979a20639316?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',4),
      ('https://d2wwnnx8tks4e8.cloudfront.net/images/app/large/5000394017641_3.JPG',5),
      ('https://i.ebayimg.com/images/g/juMAAOxyjzNRGONf/s-l300.jpg',5);

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

delete from firesale_sellernotification;