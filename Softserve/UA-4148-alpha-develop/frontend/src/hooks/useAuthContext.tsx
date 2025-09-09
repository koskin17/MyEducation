import type { AuthContextType } from "@/components/service/providers/AuthProvider";
import { createContext, useContext } from "react";

export const AuthContext = createContext<AuthContextType | null>(null);

export function useAuthContext() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuthContext must be used within an AuthProvider");
  }
  return context;
}
