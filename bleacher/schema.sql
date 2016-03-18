drop table if exists worms;
create table worms (
  id integer primary key autoincrement,
  title text not null,
  link text not null
);
