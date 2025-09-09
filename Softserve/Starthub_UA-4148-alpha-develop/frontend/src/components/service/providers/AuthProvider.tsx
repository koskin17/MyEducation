import type { SignInResponse } from "@/api/auth";
import { AuthContext } from "@/hooks/useAuthContext";
import {
  useCallback,
  useState,
  type PropsWithChildren,
  useEffect,
  useMemo,
} from "react";

export interface AuthContextType {
  user: SignInResponse["user"] | null;
  accessToken: string | null;
  refreshToken: string | null;
  login: (data: SignInResponse) => void;
  logout: () => void;
}

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<SignInResponse["user"] | null>(null);
  const [accessToken, setAccessToken] = useState<SignInResponse["access"] | null>(null);
  const [refreshToken, setRefreshToken] = useState<string | null>(null);

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    const storedToken = localStorage.getItem("accessToken");
    const storedRefresh = localStorage.getItem("refresh");

    if (storedUser && storedToken) {
      setUser(JSON.parse(storedUser));
      setAccessToken(storedToken);
      setRefreshToken(storedRefresh);
    }
  }, []);

  const login = useCallback((data: SignInResponse) => {
    setUser(data.user);
    setAccessToken(data.access);
    localStorage.setItem("user", JSON.stringify(data.user));
    localStorage.setItem("accessToken", data.access);
    localStorage.setItem("refresh", data.refresh);
  }, []);

  const logout = useCallback(() => {
    setUser(null);
    setAccessToken(null);
    setRefreshToken(null);
    localStorage.clear();
  }, []);

  const value = useMemo<AuthContextType>(
    () => ({
      user,
      accessToken,
      refreshToken,
      login,
      logout,
    }),
    [user, accessToken, refreshToken, login, logout]
  );
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
