 ### 🐼Create an ER-Diagram with [dbdiagram.io](https://dbdiagram.io) (On Browser)
***
👋 Hi everyone, I'm currently learning how to make an ER-Diagram with dbdiagram. The language used for writing is DBML (Database Markup Language), and it's super easy to learn!

![dbdiagram.io](Screenshot%202024-08-14%20003016.png)

📌 **DBML is similar to SQL language**

- **Table** = Create a new table
  `Table Entity name { Attribute: Col_name, Datatype [Primary Key] }`


```sql 
Table invoices {
  InvoiceId int [pk]
  CustomerId int
  InvoiceDate datetime
  BillingAddress nvarchar(120)
  BillingCity nvarchar(120)
}
```
- **Relationship** = Create a Relationship
```text
- = one to one
> = many to one
< = one to many
<> = many to many
```
🛸 **ex.1** 
```sql
// Crate Table
Table media_types {
  MediaTypeId int [pk]
  Name nvarchar(120)
}

Table tracks {
  TrackId int [pk]
  Name nvarchar(200)
  AlbumId int
  MeadiaTypeId int
  GenreId int
  Composer nvarchar(220)
  Milliseconds int
  Byes int
  UnitPrice numeric
}

// Create Relationship
// This Ref. is one to many relationship
Ref: media_types.MediaTypeId < tracks.MeadiaTypeId

```

![ERD](Screenshot%202024-08-14%20002050.png)

🛸**ex.2**

```sql
// Practice Create a ERDiagram
// Create entity 

Table media_types {
  MediaTypeId int [pk]
  Name nvarchar(120)
}

Table genres {
  GenreId int [pk]
  Name nvarchar(120)
}

Table playlists {
  PlaylistId int [pk]
  Name nvarchar(120)
}

Table playlist_track {
  PlaylistId int
  TrackId int
  indexes  {
    (PlaylistId,TrackId) [pk]
  }
} 

Table tracks {
  TrackId int [pk]
  Name nvarchar(200)
  AlbumId int
  MeadiaTypeId int
  GenreId int
  Composer nvarchar(220)
  Milliseconds int
  Byes int
  UnitPrice numeric
}

Table artists {
  ArtistId int [pk]
  Name nvarchar(120)
}

Table invoices {
  InvoiceId int [pk]
  CustomerId int
  InvoiceDate datetime
  BillingAddress nvarchar(120)
  BillingCity nvarchar(120)
}

Table invoice_items {
  InvoiceItemId int [pk]
  InvoiceId int
  TrackId  int
  UnitPrice numeric
  Quantity int
}

Table albums {
  AlbumId int [pk]
  Title nvarchar(160)
  ArtitsId int
}

Table customers {
  CustomerId integer [primary key]
  FirstName nvarchar(40)
  LastName nvarchar(20)
  Company nvarchar(80)
  Address nvarchar(70)
  City nvarchar(40)
  State nvarchar(40)
  Country nvarchar(40)
  PostalCode nvarchar(10)
  Phone nvarchar(24)
  Fax nvarchar(24)
  Email nvarchar(60)
  SupportRepId int
}

Table employees {
  EmployeeId int [pk]
  FirstName nvarchar(20)
  LastName nvarchar(20)
  Title nvarchar(30)
  RepostsTo int
  BirthDate datetime
  HireDate datetime
  Address nvarchar(70)
}

// Create Relatoinship
Ref: media_types.MediaTypeId < tracks.MeadiaTypeId

Ref: genres.GenreId < tracks.GenreId

Ref: playlists.PlaylistId - playlist_track.PlaylistId

Ref: playlist_track.TrackId - tracks.TrackId

Ref: artists.ArtistId < albums.ArtitsId

Ref: albums.AlbumId < tracks.AlbumId

Ref: tracks.TrackId < invoice_items.InvoiceItemId

Ref: invoice_items.InvoiceId > invoices.InvoiceId

Ref: customers.CustomerId < invoices.CustomerId

Ref: customers.SupportRepId > employees.EmployeeId
```
![END2](Screenshot%202024-08-14%20001145.png)

> Table.Ref from SQLite Tutorial 🙏🥹

<br>

📖 **Read more :** [https://docs.dbdiagram.io](https://docs.dbdiagram.io/)

<h3>Thank you for your attention 🙏🫡