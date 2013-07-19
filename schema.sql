/*

ZipTrades Database Schame
Outlined in the following Google Doc:
https://docs.google.com/spreadsheet/ccc?key=0AiMvwi9o2O9IdFRpZ0RuU2RoSXNDa21NTVpoTFNKNFE&usp=sharing

==============================================================================

SQLite3 datatypes from:
http://www.sqlite.org/datatype3.html

NULL. The value is a NULL value.
INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
BLOB. The value is a blob of data, stored exactly as it was input.

==============================================================================

Sample schema from flask documentation availabel at:
http://flask.pocoo.org/docs/tutorial/schema/

drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);

==============================================================================

Create your database by running the following command:

    sqlite3 ziptrades.db < schema.sql

*/

drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    email text not null,
    zipcode text not null,
    activated integer not null
);

drop table if exists forum_threads;
create table forum_threads (
    id integer primary key autoincrement,
    user_id integer not null,
    title text not null,
    date_created integer not null,
    date_recent integer not null
);

drop table if exists forum_posts;
create table forum_posts (
    id integer primary key autoincrement,
    user_id integer not null,
    body text not null,
    date_created integer not null,
    date_modified integer not null
);


drop table if exists listings;
create table listings (
    id integer primary key autoincrement,
    anon integer not null,
    anon_email text not null,
    user_id integer not null,
    zipcode text not null,
    title text not null,
    body text not null,
    date_created integer not null,
    date_modified integer not null
);

drop table if exists zipcodes;
create table zipcodes (
    id integer primary key autoincrement,
    zipcode text not null,
    city text not null,
    state text not null,
    latitude real not null,
    longitude real not null
);