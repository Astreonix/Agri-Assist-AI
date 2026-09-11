import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import App from './App';
import { AuthProvider } from './AuthContext';
import './styles.css';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#1d6b49', dark: '#10291f', light: '#d6e869', contrastText: '#fff' },
    secondary: { main: '#c8874c' },
    background: { default: '#f5f7f2', paper: '#ffffff' },
    text: { primary: '#18332a', secondary: '#718078' },
  },
  typography: {
    fontFamily: '"DM Sans", sans-serif',
    h1: { fontFamily: '"Fraunces", serif', fontWeight: 600 },
    h2: { fontFamily: '"Fraunces", serif', fontWeight: 600 },
    h3: { fontFamily: '"Fraunces", serif', fontWeight: 600 },
    button: { textTransform: 'none', fontWeight: 700 },
  },
  shape: { borderRadius: 6 },
  components: {
    MuiButton: { defaultProps: { disableElevation: true } },
    MuiCard: { styleOverrides: { root: { border: '1px solid #dbe4dd', boxShadow: '0 18px 45px rgba(23,54,38,.07)' } } },
  },
});

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <AuthProvider><App /></AuthProvider>
      </ThemeProvider>
    </BrowserRouter>
  </React.StrictMode>,
);
