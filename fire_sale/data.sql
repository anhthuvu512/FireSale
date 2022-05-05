delete from django_migrations where app = 'firesale';
delete from django_migrations where app = 'user';

drop table firesale_user;
drop table firesale_item;
drop table firesale_itemimage;
drop table firesale_seller;
drop table firesale_buyer;
drop table firesale_offer;
drop table user_profile;

select * from firesale_user;
select * from firesale_seller;
select * from firesale_item;
select * from firesale_itemimage;
select * from user_profile;

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
Values('https://images.unsplash.com/photo-1625229086762-f06307638717?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80',1),
      ('https://images.unsplash.com/photo-1615486261304-6978e38f377a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',2),
      ('https://images.unsplash.com/photo-1576566588028-4147f3842f27?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80',3),
      ('https://images.unsplash.com/photo-1586527484765-979a20639316?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',4);

insert into firesale_offer(price, accepted, buyer_id, item_id) values (1599, false, 1, 1)

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

create trigger CheckOfferPrice
after insert on firesale_offer
for each row execute procedure CheckOfferPrice();

