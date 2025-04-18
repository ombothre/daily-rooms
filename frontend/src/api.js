// src/api.js

const BASE_URL = 'https://daily-rooms.onrender.com/api';

export const createRoom = async (bot, body) => {
  const endpoint = `${BASE_URL}/createRoom/${bot}`;
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });

  if (!response.ok) {
    throw new Error('Failed to create room');
  }

  return await response.json();
};
