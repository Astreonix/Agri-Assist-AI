import { createContext, useContext, useEffect, useState } from 'react';
import api from './api';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem('agri_token'));
  const [profile, setProfile] = useState(null);
  const [preferences, setPreferences] = useState({ language: 'English', temperature_unit: 'metric', notifications_enabled: true });
  const [loading, setLoading] = useState(Boolean(token));

  useEffect(() => {
    if (!token) { setLoading(false); return; }
    Promise.all([api.get('/profile'), api.get('/preferences')]).then(([profileResponse, preferenceResponse]) => {
      setProfile(profileResponse.data);
      setPreferences(preferenceResponse.data);
    }).catch(() => logout()).finally(() => setLoading(false));
  }, [token]);

  async function authenticate(mode, values) {
    const { data } = await api.post(mode === 'register' ? '/auth/register' : '/auth/login', values);
    localStorage.setItem('agri_token', data.access_token);
    setToken(data.access_token);
    return data;
  }

  function logout() {
    localStorage.removeItem('agri_token');
    setToken(null);
    setProfile(null);
  }

  async function refreshProfile() {
    const { data } = await api.get('/profile');
    setProfile(data);
    return data;
  }

  async function updatePreferences(nextPreferences) {
    await api.put('/preferences', nextPreferences);
    setPreferences(nextPreferences);
  }

  return <AuthContext.Provider value={{ token, profile, setProfile, preferences, loading, authenticate, logout, refreshProfile, updatePreferences }}>
    {children}
  </AuthContext.Provider>;
}

export function useAuth() { return useContext(AuthContext); }
