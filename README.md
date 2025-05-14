Client: https://github.com/omerdynasty/message-api/releases/tag/test

# Flask Message API

A simple Flask-based API for storing, retrieving, and checking one-time messages by ID using a bearer token for authentication.

## Features

* Store messages with a unique ID
* Retrieve and delete a message by ID (one-time retrieval)
* Check if a message exists by ID without retrieving it
* Authorization via Bearer Token

## Requirements

* Python 3.7+
* pip (Python package manager)

## Setup

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install flask python-dotenv
   ```

4. **Create a `.env` file** in the root directory and add your secret key:

   ```env
   SECRET_KEY=your_secret_key_here
   ```

5. **Run the app:**

   ```bash
   python app.py
   ```

## Endpoints

### POST `/send_message/<message_id>`

Stores a message under the given ID.

**Headers:**

```http
Authorization: Bearer <SECRET_KEY>
Content-Type: application/json
```

**Body:**

```json
{
  "message": "your message here"
}
```

### GET `/get_message/<message_id>`

Retrieves and deletes the message with the given ID.

**Headers:**

```http
Authorization: Bearer <SECRET_KEY>
```

**Response:**

```json
{
  "message": "your message here"
}
```

### HEAD `/check_message/<message_id>`

Checks if a message exists with the given ID. Returns:

* `204 No Content` if exists
* `404 Not Found` if not

**Headers:**

```http
Authorization: Bearer <SECRET_KEY>
```

## License

MIT License
