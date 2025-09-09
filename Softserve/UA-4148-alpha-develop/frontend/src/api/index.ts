// src/api/axiosInstance.js
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

const refreshToken = async (token: string) => {
  const response = await axios.post(
    `${import.meta.env.VITE_API_BASE_URL}/api/refresh`,
    {
      refresh: token,
    }
  );
  return response.data;
};

axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Check if the error is 401 (Unauthorized) and request wasn't retried yet
    if (
      error.response &&
      error.response.status === 401 &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      try {
        const refresh = localStorage.getItem("refresh");
        if (!refresh) {
          console.error("No refresh token found");
          return Promise.reject(error);
        }

        const data = await refreshToken(refresh);
        
        localStorage.setItem("accessToken", data.access);
        if (data.refresh) localStorage.setItem("refresh", data.refresh);

        axiosInstance.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${data.access}`;
        originalRequest.headers["Authorization"] = `Bearer ${data.access}`;

        return axiosInstance(originalRequest);
      } catch (err) {
        console.error("Token refresh failed", err);
        // Optionally clear tokens and redirect to login
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refresh");
        // window.location.href = "/login"; // if needed
        return Promise.reject(err);
      }
    }

    return Promise.reject(error);
  }
);


export default axiosInstance;
