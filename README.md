# To-do's boilerplate
FastAPI

```
Dockerfile, MySQL localhost (111) error
```
## venv in local
```
cd to-do-app/fastapi

[create venv]
python venv -m venv

[access venv]
venv\Scripts\Activates.ps1 (windows)
source venv/bin/activate (mac)

[select interpreter]
get-command python (windows)
which python (mac)

[install library]
pip install -r requirements.txt

[run app]
uvicron main:app --reload
```
## Database
```
CREATE DATABASE IF NOT EXISTS `todo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `todo`;

CREATE TABLE `todo`.`user` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
ENGINE = InnoDB;

CREATE TABLE `todo`.`todo` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `content` VARCHAR(255) NOT NULL,
  `is_complete` BOOLEAN NOT NULL DEFAULT FALSE,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  FOREIGN KEY (`user_id`) REFERENCES `todo`.`user` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE)
ENGINE = InnoDB;
```
